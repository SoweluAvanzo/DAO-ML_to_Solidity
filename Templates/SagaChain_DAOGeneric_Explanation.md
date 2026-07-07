# SagaChain DAO Templates — Design Notes

This document explains how the SagaChain-inspired DAO templates in this folder were derived from
`Templates/DAOOptimizedGeneric_1_0_0.jinja`, and how they apply the modelling language of the
**SagaChain Technical Whitepaper** (PraSaga, D. Beberman / M. Holdmann / J. Moore) to this
project's DAO-ML logical model. There are now two variants, covering §1–8 below and §9
respectively:

1. **`SagaChain_DAOGeneric_1_0_0.py.jinja`** — a **plain, standalone, runnable Python module**.
   No Solidity, no external dependency. Fully rendered, executed, and tested (§7).
2. **`SagaChain_DAOGeneric_Deploy.spy.jinja` + `SagaChain_DAOGeneric_Invoke.spy.jinja`** (§9) —
   the *same* modelling, re-expressed as real **SagaPython transaction-script** syntax
   (`@SagaClass`/`@SagaMethod`/`SagaField`), informed by directly reading the actual
   `sagapython` reference implementation. This variant can only run inside SagaPython's own
   Docker/LevelDB/signing toolchain, which is not available in this environment — see §9's
   Caveats before relying on it.

## 1. What was read first

Before writing anything, the following were read in full to make sure the new template is a
faithful, drop-in-compatible generalization rather than an unrelated rewrite:

- `Templates/DAOOptimizedGeneric_1_0_0.jinja` — the reference Solidity template: state layout
  (packed role/committee bitmasks, `role_permissions`), the `controlledBy`/`hasPermission`
  modifiers, the constructor, committee initialization, role/permission management functions,
  permission stub functions, and `canVote`/`canPropose`.
- `src/postprocessing/model_translation/solidity/optimized/jinja/t_o_sol_jinja_1_0_0.py` — the
  Python translator that builds the **exact context dict** handed to that Jinja template
  (`translate_dao()`). This is the ground truth for every variable name/shape the new template
  can rely on.
- `src/model/*.py` (`dao.py`, `role.py`, `committee.py`, `permission.py`, `governance_area.py`,
  `aggregable_entity.py`, `base_entity.py`, `enums/user_functionalities_group_size.py`) — the
  language-independent DAO-ML model these templates both consume.
- `README.md` — the three existing translation schemes (`optimized`/`simple`/`standard`) and the
  overall translator architecture.

## 2. The key finding that shaped the design

`src/model/dao.py` already carries a `governance_areas: dict[str, GovernanceArea]` collection,
and every `Permission` already carries a `ref_gov_area` field pointing at one. **Nothing in the
Solidity translator (`t_o_sol_jinja_1_0_0.py`) ever reads either of these** — `dao.governance_areas`
is populated by the parser/postprocessing stage and then simply never surfaces in
`dao_specific_data_translated`.

That unused hook is almost exactly SagaChain's **Operational Smart Asset** concept (Whitepaper
§6, §8): a named, governed domain whose lifecycle and parameters can only change through a
committee vote. So rather than inventing a parallel governance mechanism, this template turns
every distinct `ref_gov_area` value found among a DAO's permissions into one governed
`OperationalSmartAsset`, reusing the DAO's *existing* role/committee/permission system as the
"Registry of Committee Members" (§8.1) — no new voter/committee concept was introduced.

## 3. Concept mapping (SagaChain → this template)

| SagaChain Whitepaper concept | §   | Python realization |
|---|---|---|
| First-class object, identified by an immutable `object_identifier` | 5.1 | Each Role/Committee is one slot in `ALL_ROLES`, indexed by position |
| Object "state" = its field values | 5.2 | The packed `int` value in `ALL_ROLES[i]`: low bits = index, high bits = control bitmask (identical encoding to the Solidity template) |
| Directed object graph within an account / control relation | 5.3 | `can_control()` / `_require_controlled_by()` — the same bit arithmetic as Solidity's `canControl`/`controlledBy`, transliterated 1:1 |
| `ClassReferenceAsset` — a reference held in the owner's account; the underlying object never moves | 5.5 | The `roles: dict[str, int]` mapping: an address holds a *reference* (an `int` role id) to a role/committee "object" that is itself immutable and shared |
| Extensible Smart Object Asset (XSOA) | 6 | `OperationalSmartAsset` dataclass: one per DAO-ML `GovernanceArea` in use |
| "Registry of Committee Members Asset" | 8.1 | Reused as-is: whichever role/committee already holds the governing permission bit for that asset |
| "Governance Voting Asset" (FIFO change-request queue, one outstanding request per asset) | 8.1, 8.3 | `ChangeRequest` dataclass + `propose_change_request` / `vote_change_request` / `finalize_change_request` + `_open_request_by_asset` |
| Governance capabilities: Start/Stop/Pause/Reset, Parameter Change, Algorithm Change, Delete Asset, Custom | 8.1 | `ChangeType` enum, applied in `_apply_change_request` |
| "The new function must match the exact signature of the old one" (algorithmic change) | 8.3 | Enforced literally via `inspect.signature(new) == inspect.signature(old)` before an `ALGORITHM_CHANGE` is even accepted — Python callables make this a direct, no-proxy-needed analogy |
| "Majority / super-majority / unanimous" governance mandate | 8.3 | `MajorityType` enum + `_threshold_met()` |
| Community plenary vote for major changes, "one person, one vote — not weighted by tokens/permissions held" | 8.2, 8.3 | `OperationalSmartAsset.requires_community_ratification`; the plenary round in `vote_change_request` only checks `sender in self.roles` (any DAO member), never a permission bit |
| "A governance asset is immutable once instantiated" | 8.1 | The propose/vote/finalize machinery is never itself a valid `ChangeType` target — only `OperationalSmartAsset` entries can be changed |
| Digital-GDP-style "basket of assets" (one Fractionalization Object aggregating several source objects) | 5.3.4, 6.3 | Not re-implemented: the DAO-ML `Committee.member_entities` already models this (a committee aggregating several roles under one federated entity) — noted here for completeness, no new code needed |

## 4. Deliberate simplifications vs. the Whitepaper / the Solidity template

- **No Solidity storage-packing.** `id_var_type`/`perm_var_type` (`uint8`…`uint256` selection)
  and `is_role_access_optimized` (array-vs-mapping storage) exist in the Solidity translator
  purely to minimize on-chain storage cost. Python integers are arbitrary-precision and `dict`
  lookups are O(1) regardless, so the new template ignores those three context variables
  entirely and always uses plain `int` and `dict[int, int]`.
- **No on-chain "address" for algorithms.** SagaChain's Solidity realization would need an
  external contract address for a swappable "algorithm" (which is what the Diamond/EIP-2535
  facet files already in `Templates/` are for). In Python, a callable *is* a first-class value,
  so `OperationalSmartAsset.algorithm` is simply reassigned — no proxy/indirection needed.
- **Plenary quorum is relative, not absolute.** The base DAO-ML model has no enumerable roster of
  "every address that currently holds a role" (only a `roles: dict[str, int]` populated
  on-demand), so there is no way to know the *total* eligible plenary electorate at compile time.
  The plenary round therefore resolves by relative majority among whoever actually voted before
  the deadline (`plenary_votes_for > plenary_votes_against`), not a quorum against total
  membership. This is flagged explicitly in the code (`vote_change_request`) rather than silently
  assumed.
- **`visibility`/`visibility_committee_initialization_function` are dropped.** Python has no
  `public`/`internal`/`external` distinction at the language level; "internal" is expressed the
  usual Python way — a leading underscore on helper/guard methods (`_require_permission`,
  `_apply_change_request`, …) — rather than by threading the Solidity `visibility` string through
  the template.

## 5. A pre-existing bug found (and fixed, in this template only)

While porting `initializeCommittees`, `DAOOptimizedGeneric_1_0_0.jinja` does this:

```
{% for c in committees_names_list %}
roles[_{{space_to_underscore_fn(c)}}] = all_roles[{{loop.index0}}]; // {{space_to_underscore_fn(c)}}{% endfor %}
```

`all_roles` is populated as `[...roles..., ...committees...]` (roles first, see the state-variable
block earlier in the same file), but this loop indexes it with a **fresh, committee-local**
`loop.index0` (0, 1, 2, … within `committees_names_list` alone) instead of
`roles|length + loop.index0`. Whenever a DAO has at least one Role (i.e. always, in practice — a
DAO always has an Owner role), this assigns each initialized committee member the *wrong* entity's
packed control-bitmask (a Role's, not that Committee's).

This template uses the corrected form:

```
self.roles[{{ space_to_underscore_fn(c) }}] = self.ALL_ROLES[{{ roles|length + loop.index0 }}]
```

This was **not** back-ported into `DAOOptimizedGeneric_1_0_0.jinja` (out of scope for this task),
but it should be flagged to whoever next touches that file.

## 6. Context-variable contract

Reused as-is from `t_o_sol_jinja_1_0_0.py`'s existing context (no Python translator changes
needed to exercise everything except the governance layer): `dao_name`, `mission_statement`,
`roles`, `committees`, `committees_names_list`, `states_variables__functionalities_ids`,
`roles_computed_data`, `committees_computed_data`, `entities_amount`,
`control_relation_id_bit_size`, `control_relation_mask`, `id_mask`, `permissions`,
`permission_index_by_id`, `function_permission_name_by_id`, `entities_permissions`,
`constructor_parameters`, `dao_conditions`, `voting_conditions`, `proposal_conditions`,
`assignment_conditions`, `dao_owner`, `voting_function`, `proposal_function`,
`space_to_underscore_fn`.

New, all optional with safe in-template defaults (no Python translator changes required to use
this template at all — the governance layer is simply empty if a DAO defines no `ref_gov_area`
on any permission):

- The set of governed assets is *derived*, not supplied: `permissions | selectattr('ref_gov_area')
  | groupby('ref_gov_area')`. If no permission sets `ref_gov_area`, `self.operational_assets` is
  simply `[]` and the whole governance layer is inert but present (all its methods still exist,
  they just have nothing to act on).
- `governance_default_voting_duration_seconds` (int, seconds) — defaults to `259200` (3 days) if
  not supplied in the context.

Dropped (Solidity-only, see §4): `id_var_type`, `perm_var_type`, `is_role_access_optimized`,
`visibility`, `visibility_committee_initialization_function`.

## 7. How this was validated

Since this template's only real risk is Jinja-driven Python indentation (unlike Solidity, Python
has no braces, so a mis-scoped `{% if %}` can silently produce an `IndentationError` or a subtly
wrong logical grouping), it was rendered and executed, not just read:

1. Rendered against **4 structural fixtures** (`jinja2.Template(...).render(...)`) covering: a
   DAO with committees + governance areas + all three condition kinds populated; a DAO with
   `dao_conditions` set but only `assignment_conditions` populated; a DAO with `dao_conditions`
   set but *none* of the three specific condition dicts populated (the empty-`for`-body edge
   case, guarded with an explicit `pass`); and a minimal DAO with no committees/conditions/
   governance areas at all. Each output was parsed with `ast.parse` to confirm valid Python.
2. The "full" rendering was then actually **imported and executed** end-to-end: constructing the
   DAO, `assign_role`/`revoke_role`, `grant_permission`/`revoke_permission`, `can_control`
   rejecting a Member trying to govern another Member, `initialize_committees` (including the
   fixed indexing from §5), a full `ChangeRequest` lifecycle (parameter change, plenary
   ratification requiring a second round, a non-member correctly rejected from the plenary vote,
   an algorithm swap accepted, and a signature-mismatched algorithm swap correctly rejected), and
   the FIFO "one outstanding change request per asset" rule.

## 8. Wiring this into the CLI pipeline (not done here — future work)

This deliverable is the template itself, per request; it is not yet wired into `run_cmd.py`/the
`post_processing_transformation` flag set (`sol`, `sol_tests`, `asm`, `json`). Doing so would mean
adding a `"python"` target that mirrors
`src/postprocessing/model_translation/solidity/optimized/jinja/t_o_sol_jinja_1_0_0.py`'s
`translate_dao()` — the same context values, since §6 above intentionally reuses that exact
contract, plus the two new optional keys. No other pipeline change should be required.

## 9. The SagaPython transaction-script variant

A follow-up request asked to refactor the template to actually use SagaChain's real Python
classes/decorators, pointing at the reference implementation:
`https://code.prasaga.com/sagachain/sagapython`. The repo was cloned and inspected directly
(source reads plus two parallel exploration passes) before writing any code, because the answer
to "what does 'use their real classes' even mean here" turned out to be non-obvious.

### 9.1 What SagaPython actually is

- **Not a library.** No `setup.py`/`pyproject.toml` anywhere in the repo. `SagaClass`/
  `SagaMethod`/`SagaField` (aliases of `CMIclassdec`/`CMIMethoddec`/`CMIFieldEx` in
  `sagapython/product/cmidecorators.py`, bound in `sagaclasseswrapper.py`) only *record metadata
  into module-global lists* at decoration time. The real class object is created later by
  `BuildCMIClasses()` → `metaclass.new(...)`, which needs a resolvable owner account already
  present in an object database.
- **Transaction scripts aren't `import`able.** They follow a fixed `__hdr()` / `__CMIClasses()` /
  `__body()` contract. `spexec.py` first `ast.parse()`s the *whole file* (so the file as a whole
  must be syntactically valid Python — this is exactly what our own verification in §9.4 checks),
  then extracts each named function's subtree, dedents its source (`stripfunction()`), recompiles
  it standalone, and `exec()`s it with CMI-injected globals (`SagaClass`, `ClsObjVar`, `LOID`,
  `Log`, `CMIConst`, `SPDecConst`, …) that don't exist via any normal `import`.
- **Real execution requires their full toolchain**: an `edsig` keypair, `spclient` to sign the
  script, then `sptransactionexecutor` to run it against a LevelDB-backed object-state database
  (`ObjectDataBase.py`, normally reached via `posix_ipc`/protobuf), all inside their Docker
  container. Their own README says outright: *"Direct access to Sagapython is not currently
  enabled"* and *"This readme is out of date and cannot be relied upon."* Full setup also needs a
  `.env` file from a private PraSaga SharePoint link we don't have access to.
- **`sputils.py` — a module `spexec.py`'s `readHeadTail()` imports — doesn't exist in this cloned
  snapshot at all.** Consistent with this, no real example script defines a `__tail()` function
  (only `__hdr`/`__CMIClasses`/`__body`), even though `readHeadTail()` appears to require one. We
  followed the worked examples (the more reliable ground truth, since they're the artifacts
  actually meant to run) rather than that possibly-stale code path.
- **No governance/committee/voting/permission code exists anywhere in the repo** (exhaustive grep
  across every `.py` file). SagaChain's whole §8 (Registry of Committee Members, Governance Voting
  Asset, Operational Smart Asset lifecycle, plenary voting) is whitepaper-only — SagaPython
  implements strictly the lower-level object/class model (§5/§6: classes, fields, methods,
  single-owner ACL checks via `SPClassVerify.py`). There is also no `ClassAsset` base class with
  description/proof-of-ownership fields — `SPClassObject`'s only fields are
  type/owner/refcount/transient.

Given this, the user chose a **hybrid** approach: keep `SagaChain_DAOGeneric_1_0_0.py.jinja`
(§1–8) exactly as-is as the tested, standalone default, and add a second variant that renders
real SagaPython syntax, with the explicit understanding that it can't be executed here and that
all governance/permission logic is still our own design, merely re-expressed in their idiom.

### 9.2 Files

- **`Templates/SagaChain_DAOGeneric_Deploy.spy.jinja`** — one `__hdr()`/`__CMIClasses()`/
  `__body()` script (matching `testtransactionscripts/classassetexample.py` and
  `sagafield_decorator.py`) that declares three sibling CMI classes and deploys the DAO:
  - **`{{ dao_name }}`** — the DAO itself: `roles`/`role_permissions` as `SagaField`s (same
    packed-bitmask encoding as §1–8), plus `@SagaMethod()` ports of `assign_role`/`revoke_role`/
    `grant_permission`/`revoke_permission`/`has_role`/`has_permission`/`can_control`/
    `initialize_committees`/the per-permission stub methods/`can_vote`/`can_propose`.
  - **`OperationalSmartAsset`** and **`ChangeRequest`** as their **own separate `@SagaClass`
    objects** (each gets its own LOID) — a deliberate upgrade over §1–8's plain dataclasses,
    truer to "objects are first-class citizens... methods define valid operations" (Whitepaper
    §5.1). `OperationalSmartAsset` owns `propose_change_request`/`vote_change_request`/
    `finalize_change_request`/`execute_algorithm`, holding a `dao_ref` field back to its DAO for
    permission checks; `ChangeRequest` owns its own vote-tallying and `finalize()` logic.
  - `__body()` deploys the DAO and one `OperationalSmartAsset` per DAO-ML `GovernanceArea` (same
    `permissions | selectattr('ref_gov_area') | groupby('ref_gov_area')` derivation as §1–8),
    logging each new object's LOID.
- **`Templates/SagaChain_DAOGeneric_Invoke.spy.jinja`** — one generic, parameterized follow-on
  script (matching `testtransactionscripts/classassetupdate.py`'s "load an existing object by
  LOID, call a method on it" pattern: `LOID(...)` → `ClsObjVar(...)` → `.SomeMethod(...)`).
  Covers **every** DAO interaction by taking `target_object_loid`/`target_method`/`target_args`
  as render-time parameters, instead of one near-duplicate script per method.

Both use the `.spy.jinja` extension (not `.py.jinja`) specifically so the rendered output is not
mistaken for directly runnable Python.

### 9.3 Concept/API mapping and design choices

| §1–8 Python construct | SagaPython real equivalent |
|---|---|
| `class X:` (dataclass or plain class) | `@SagaClass(CMIConst.SPClassObject) class X:` (verified signature: `CMIclassdec(*baselist, owner=None, metaclass=..., ...)`) |
| dataclass field | `SagaField(spff=SPDecConst.spfread\|spfwrite\|spfprotected, spftype=...)` — verified directly against `cmidecorators.py`'s `CMIFieldEx(*args, **kwargs)` (first positional arg must be the field name in general, though every field here uses the class-body-assignment form seen in the real examples, e.g. `name = SagaField(spff=..., spftype=str)`); the flag/type kwargs (`spfread`/`spfwrite`/`spfprotected`, `spftype=str`/`int`/`bool`) were also checked against real values (`SPDecConst.spfread = 2**0`, etc.) rather than guessed |
| method | `@SagaMethod() def ...():` (verified: `CMIMethoddec(*args, **kwargs)`) |
| `OperationalSmartAsset.algorithm` (bare Python callable, swapped directly) | `algorithm_ref`: a field holding a *reference to another CMI object* that implements `execute(asset, data)`; "algorithm change" swaps which object the reference points at. This maps the whitepaper's "new function must match the exact signature of the old one" onto SagaPython's actual object-reference-and-method-dispatch model more naturally than a raw callable would |
| calling a helper across objects (`self._require_permission(...)`) | Not used as a shared private helper in this variant: every method inlines its own permission/control check instead of calling a shared method on `self`. Reason: the only cross-call pattern actually evidenced in the real examples is a **parent object calling a method on a held child reference** (`self.ob.getName()` in `sagafield_decorator.py`); a `self`-to-`self` call to another decorated method has no confirmed precedent, so we avoided depending on it |
| `ALL_ROLES` class constant, indexed at call time | **Not used.** Every small integer constant (bit widths, masks, entity counts, packed role/committee ids, permission indices) is inlined as a literal directly into each generated method's source at Jinja render time. Reason: SagaPython persists and independently re-execs each `@SagaMethod`'s source per call (`CMIClass.py`'s `ClassTableEntry.DoMethod`/`DoMethodCompile`, which `base64`-decodes and `exec()`s one method body at a time) — nothing found guarantees a closure over an outer scope, or a plain (non-`SagaField`) class attribute, survives into that later, separate `exec()` |
| `inspect.signature(new) == inspect.signature(old)` check | Not reproduced — SagaPython has no equivalent hook exposed in what we read; the object-reference swap above is the closest faithful analogue |

### 9.4 Verification — and what could *not* be verified

Full CMI execution is not reproducible here (§9.1). What was actually checked, mirroring §7's
rigor as closely as the situation allows:

1. Rendered `SagaChain_DAOGeneric_Deploy.spy.jinja` against two structural fixtures (with and
   without committees/governance areas) and `SagaChain_DAOGeneric_Invoke.spy.jinja` both with
   filled-in and default placeholder values. For every rendering, ran `ast.parse()` on the
   **entire file** — this is not an arbitrary proxy check: it is literally the first thing
   `spexec.py`'s `readHeadTail()` does to the whole script before extracting individual
   functions, so a passing `ast.parse()` here is a meaningful, faithful integrity check even
   without the rest of their stack.
2. Confirmed the top-level function set found by `ast.parse()` matches the real contract
   (`__hdr`, `__CMIClasses`, `__body` for Deploy; `__hdr`, `__body` for Invoke).
3. Confirmed every `SagaClass(...)`/`SagaMethod(...)`/`SagaField(...)` call in the rendered output
   matches the signatures verified directly against `cmidecorators.py` (§9.3), by inspection.
4. **Not done, and not claimed:** behavioral correctness. Nothing here confirms the generated
   scripts would actually execute successfully against a real SagaPython object-state database —
   only that they're syntactically well-formed per the one check we could faithfully reproduce.
   Treat this variant as an informed, best-effort translation of already-designed, already-tested
   logic (§1–8) into SagaPython's real declaration syntax — not as something proven to run.
