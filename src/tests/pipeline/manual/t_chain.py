
import src.pipeline.pipeline_manager as pmp
import src.pipeline.pipeline_item as pi

import src.pipeline.pipeline_items_chained as pc
import src.pipeline.utilities.pi_chain_store_releaser_branching as pi_chain_store
import src.pipeline.utilities.pi_printer as pri
import src.pipeline.utilities.pi_str as pstr
import src.pipeline.utilities.pi_int as pint
import src.pipeline.utilities.pi_any_value as pval
import src.tests.pipeline.shared.pi_add_mul as pi_add_mul


if __name__ == "__main__":
    print("START t_chain\n")
    pm = pmp.PipelineManager()

    #

    k_start_str = "k_start_str"
    start_str = pstr.PIStr(
        pi.PIData(k_start_str, None), "START")
    pm.addItem(start_str)

    k_printer_start = "k_printer_start"
    printer_start = pri.PIPrinter(
        pi.PIData(k_printer_start, [k_start_str]), None, True)
    pm.addItem(printer_start)

    #

    # 7 + 2 * (30 + 4*5) = 107
    equation_start_depenencies = [k_printer_start]
    # ... constants
    k_p_int_addendum_7 = "k_p_int_addendum_7"
    p_int_addendum_7 = pint.PIInt(
        pi.PIData(k_p_int_addendum_7, equation_start_depenencies), val=7)
    pm.addItem(p_int_addendum_7)
    k_p_int_factor_2 = "k_p_int_factor_2"
    p_int_factor_2 = pint.PIInt(
        pi.PIData(k_p_int_factor_2, equation_start_depenencies), val=2)
    pm.addItem(p_int_factor_2)
    k_p_int_addendum_30 = "k_p_int_addendum_30"
    p_int_addendum_30 = pint.PIInt(
        pi.PIData(k_p_int_addendum_30, equation_start_depenencies), val=30)
    pm.addItem(p_int_addendum_30)
    k_p_int_factor_4 = "k_p_int_factor_4"
    p_int_factor_4 = pint.PIInt(
        pi.PIData(k_p_int_factor_4, equation_start_depenencies), val=4)
    pm.addItem(p_int_factor_4)
    k_p_int_factor_5 = "k_p_int_factor_5"
    p_int_factor_5 = pint.PIInt(
        pi.PIData(k_p_int_factor_5, equation_start_depenencies), val=5)
    pm.addItem(p_int_factor_5)
    # ... 4*5
    k_p_4__5 = "k_p_4__5"
    p_4__5 = pi_add_mul.PIAddMult(pi.PIData(k_p_4__5, [k_p_int_factor_4, k_p_int_factor_5]),
                                  scalar=1,
                                  is_addition=False
                                  )
    pm.addItem(p_4__5)
    # ... 30 + (4*5) = fifty
    k_p_30___4__5 = "k_p_30___4__5"
    p_30___4__5 = pi_add_mul.PIAddMult(pi.PIData(k_p_30___4__5, [k_p_int_addendum_30, k_p_4__5]),
                                       scalar=0,
                                       is_addition=True
                                       )
    pm.addItem(p_30___4__5)
    # ... 2 * fifty
    k_p_hundred = "k_p_hundred"
    p_hundred = pi_add_mul.PIAddMult(pi.PIData(k_p_hundred, [k_p_int_factor_2, k_p_30___4__5]),
                                     scalar=1,
                                     is_addition=False
                                     )
    pm.addItem(p_hundred)
    # ... equation
    k_p_equation = "k_p_equation"
    p_equation = pi_add_mul.PIAddMult(pi.PIData(k_p_equation, [k_p_int_addendum_7, k_p_hundred]),
                                      scalar=0,
                                      is_addition=True
                                      )
    pm.addItem(p_equation)

    k_p_equation_val_store = "k_p_equation_val_store"
    p_equation_val_store = pi_chain_store.PIChainStoreReleaserBranching(
        pi.PIData(k_p_equation_val_store, [k_p_equation]))
    pm.addItem(p_equation_val_store)

    #

    k_printer_equation_finished = "k_printer_equation_finished"
    printer_equation_finished = pri.PIPrinter(
        pi.PIData(k_printer_equation_finished, [k_p_equation_val_store]), "Equation calculated, starting chain", from_input=False)
    pm.addItem(printer_equation_finished)

    #

    # now, the chain

    k_printer_pre_equation = "k_printer_pre_equation"
    printer_pre_equation = pri.PIPrinter(
        pi.PIData(k_printer_pre_equation, [k_printer_equation_finished]), "Equation result:", from_input=False)
    k_printer_equation_result = "k_printer_equation_result"
    printer_equation_result = pri.PIPrinter(
        pi.PIData(k_printer_equation_result, [k_p_equation_val_store]), None, from_input=True)
    # .. the actual branching
    k_p_branching_eq_store = "k_p_branching_eq_store"
    p_branching_eq_store = pi_chain_store.PIChainStoreReleaserBranching(
        pi.PIData(k_p_branching_eq_store))
    k_p_branch_consumer = "k_p_branch_consumer"
    p_branch_consumer = pi_add_mul.PIAddMult(pi.PIData(k_p_branch_consumer, [k_p_branching_eq_store]),
                                             scalar=1000,
                                             is_addition=False
                                             )
    k_p_printer_branch = "k_p_printer_branch"
    p_printer_branch = pri.PIPrinter(
        pi.PIData(k_p_printer_branch, [k_p_branch_consumer]), None, from_input=True)

    chain_pi: list[pi.PipelineItem] = [
        printer_pre_equation,
        p_equation_val_store,
        p_branching_eq_store,
        printer_equation_result,
        p_branching_eq_store,
        p_branch_consumer,
        p_printer_branch
    ]
    k_p_chain = "k_p_chain"
    p_chain = pc.PIChained(
        pi.PIData(k_p_chain, [k_printer_equation_finished]), chain_pi)
    pm.addItem(p_chain)

    #

    k_printer_chain_finished = "k_printer_chain_finished"
    printer_chain_finished = pri.PIPrinter(
        pi.PIData(k_printer_chain_finished, [k_p_chain]), "chain finished", from_input=False)
    pm.addItem(printer_chain_finished)

    #

    k_p_eq_negativer_afterChain = "k_p_eq_negativer_afterChain"
    p_eq_negativer_afterChain = pi_add_mul.PIAddMult(pi.PIData(k_p_eq_negativer_afterChain, [k_p_equation_val_store, k_printer_chain_finished]),
                                                     scalar=-1,
                                                     is_addition=False
                                                     )
    pm.addItem(p_eq_negativer_afterChain)
    k_printer_pre_eq_neg = "k_printer_pre_eq_neg"
    printer_pre_eq_neg = pri.PIPrinter(
        pi.PIData(k_printer_pre_eq_neg, [k_p_eq_negativer_afterChain, k_printer_chain_finished]), "\n\nEquation negated:", from_input=False)
    pm.addItem(printer_pre_eq_neg)
    k_printer_eq_neg = "k_printer_eq_neg"
    printer_eq_neg = pri.PIPrinter(
        pi.PIData(k_printer_eq_neg, [k_p_eq_negativer_afterChain, k_printer_pre_eq_neg]), None, from_input=True, should_warning_nonStr_nonList=False)
    pm.addItem(printer_eq_neg)

    #
    # END preparation -> RUN
    #

    print("RUN\n\n\n")
    outputs = pm.runPipeline()
    print("\n\n\nEND")


# python -m src.tests.pipeline.manual.t_chain > TEST_CHAIN.txt
