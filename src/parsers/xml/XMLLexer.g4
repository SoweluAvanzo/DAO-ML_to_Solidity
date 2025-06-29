
lexer grammar XMLLexer;

// Default "mode": Everything OUTSIDE of a tag
COMMENT : '<!--' .*? '-->';
CDATA   : '<![CDATA[' .*? ']]>';
/** Scarf all DTD stuff, Entity Declarations like <!ENTITY ...>,
 *  and Notation Declarations <!NOTATION ...>
 */
DTD       : '<!' .*? '>' -> skip;
EntityRef : '&' Name ';';
CharRef   : '&#' DIGIT+ ';' | '&#x' HEXDIGIT+ ';';
SEA_WS    : (' ' | '\t' | '\r'? '\n')+;

OPEN         : '<'       -> pushMode(INSIDE);
XMLDeclOpen  : '<?xml' S -> pushMode(INSIDE);
SPECIAL_OPEN : '<?' Name -> more, pushMode(PROC_INSTR);

TEXT: ~[<&]+; // match any 16 bit char other than < and &

// ----------------- Everything INSIDE of a tag ---------------------
mode INSIDE;

//
DIAGRAM: 'DAO-ML_diagram';
DAO: 'DAO';
ROLE: 'Role';
COMMITTEE: 'Committee';
PERMISSION: 'Permission';
GOV: 'GovernanceArea';
//relations
ASSOCIATION: 'associated_to';
CONTROL: 'is_controlled_by';
AGGREGATES: 'aggregates';
FEDERATES: 'federates_into';

// Lexer attribute rules
DAOID : 'DAO_ID';
DAONAME : 'DAO_name';
MISSIONSTATEMENT : 'mission_statement';
HIERARCHICALINHERITANCE : 'hierarchical_inheritance';
ROLEID : 'role_ID';
ROLENAME : 'role_name';
ROLEASSIGNMENTMETHOD : 'role_assignment_method';
COMMITTEEID : 'committee_ID';
COMMITTEEDESCRIPTION : 'committee_description';
NAGENTMIN : 'n_agent_min';
NAGENTMAX : 'n_agent_max';
DMMETHOD : 'decision_making_method';
VOTINGCONDITION : 'voting_condition';
PROPOSALCONDITION : 'proposal_condition';
PERMISSIONID : 'permission_ID';
REF_GOV_AREA : 'ref_gov_area';
ALLOWEDACTION : 'allowed_action';
AGENTTYPE: 'agent_type';
PERMISSIONTYPE : 'permission_type';
FEDERATIONLEVEL : 'federation_level';
AGGREGATIONLEVEL : 'aggregation_level';

CLOSE         : '>'  -> popMode;
SPECIAL_CLOSE : '?>' -> popMode; // close <?xml...?>
SLASH_CLOSE   : '/>' -> popMode;
SLASH         : '/';
EQUALS        : '=';
STRING        : '"' ~[<"]* '"' | '\'' ~[<']* '\'';
Name          : NameStartChar NameChar*;
S             : [ \t\r\n] -> skip;

DOUBLE_TICK   : '"';

UNIQUEID_LITERAL: 'uniqueID';
UNIQUEID_PREFIX: 'dao';

fragment HEXDIGIT: [a-fA-F0-9];

fragment DIGIT: [0-9];

fragment NameChar:
    NameStartChar
    | '-'
    | '.'
    | DIGIT
    | '\u00B7'
    | '\u0300' ..'\u036F'
    | '\u203F' ..'\u2040'
;

fragment NameStartChar:
    [_:a-zA-Z]
    | '\u2070' ..'\u218F'
    | '\u2C00' ..'\u2FEF'
    | '\u3001' ..'\uD7FF'
    | '\uF900' ..'\uFDCF'
    | '\uFDF0' ..'\uFFFD'
;

fragment UuidV4Separator: '-' | '_';

fragment HEX_4
    : HEXDIGIT HEXDIGIT HEXDIGIT HEXDIGIT
    ;

UUIDV4:
    HEX_4 HEX_4 UuidV4Separator HEX_4 UuidV4Separator HEX_4 UuidV4Separator HEX_4 UuidV4Separator HEX_4 HEX_4 HEX_4
    ;

UNIQUEID: UNIQUEID_PREFIX UuidV4Separator UUIDV4;

// ----------------- Handle <? ... ?> ---------------------
mode PROC_INSTR;

PI     : '?>' -> popMode; // close <?...?>
IGNORE : .    -> more;