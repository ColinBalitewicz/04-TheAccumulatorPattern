"""
This module lets you practice the ACCUMULATOR pattern
in several classic forms:
   SUMMING:    total = total + number
   COUNTING:   count = count + 1
   AVERAGING:  summing and counting combined
and
   FACTORIAL:  x = x * k

Subsequent modules let you practice the ACCUMULATOR pattern
in its "in graphics" form:
   IN GRAPHICS:   x = x + pixels

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher, Mark Hays,
         Aaron Wilkin, their colleagues, and Colin Balitewicz.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import math
import builtins  # Never necessary, but here for pedagogical reasons


# -----------------------------------------------------------------------------
# Students: As you work each of these problems, ask yourself:
#   1. Do I need a loop?
#      If so, HOW MANY LOOPS?
#
#   2. Where I need a loop, what needs to happen:
#        -- BEFORE the loop?
#        -- IN the loop?
#        -- AFTER the loop?
# -----------------------------------------------------------------------------
def main():
    """ Calls the   TEST   functions in this module. """
    run_test_sum_from()
    run_test_factorial()
    run_test_count_cosines_from()
    run_test_sum_unit_fractions_from()


# -----------------------------------------------------------------------------
# Students: READ the  run_test_sum_from  function that follows this comment.
# -----------------------------------------------------------------------------
def run_test_sum_from():
    """ Tests the   sum_from   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_from   function:')
    print('--------------------------------------------------')

    # -------------------------------------------------------------------------
    # These first two tests use an ORACLE for testing,
    # that is, a way to get the answer by using some other approach
    # that is known to work correctly.
    #   The oracle here is the   builtins.sum    function.
    # -------------------------------------------------------------------------

    # Test 1:
    answer_from_oracle = builtins.sum(range(6, 10))
    answer_from_my_code = sum_from(6, 9)
    print('Test 1 expected (from oracle):', answer_from_oracle)
    print('       actual (from my code): ', answer_from_my_code)

    # Test 2:
    answer_from_oracle = builtins.sum(range(100, 10001))
    answer_from_my_code = sum_from(100, 10000)
    print('Test 2 expected (from oracle):', answer_from_oracle)
    print('       actual (from my code): ', answer_from_my_code)

    # -------------------------------------------------------------------------
    # The next test uses a KNOWN answer (usually computed by hand).
    #   (Everyone "knows" that the sum from 0 to 3 is 0+1+2+3, i.e. 6.)
    # -------------------------------------------------------------------------

    # Test 3:
    answer_from_by_hand = 6
    answer_from_my_code = sum_from(0, 3)
    print('Test 3 expected (from by-hand):', answer_from_by_hand)
    print('       actual (from my code):  ', answer_from_my_code)

    # -------------------------------------------------------------------------
    # The next test uses a FORMULA answer (which is one kind of ORACLE answer)
    # that uses the formula:
    #     m + (m+1) + (m+2) +  ...  + n  =  (m + n) * (n - m + 1) / 2
    # -------------------------------------------------------------------------

    # Test 4:
    answer_from_formula = (53 + 4999) * (4999 - 53 + 1) // 2
    answer_from_my_code = sum_from(53, 4999)
    print('Test 4 expected (from formula):', answer_from_formula)
    print('       actual (from my code):  ', answer_from_my_code)

# -----------------------------------------------------------------------------
# DONE: 2.
#   When you have READ the above  run_test_sum_from  function,
#   asking questions as needed, and you feel that you (mostly, at least)
#   understand it, and you feel that you understand from the example:
#     -- what an ORACLE answer is
#     -- what a KNOWN (typically, BY-HAND) answer is
#     -- what a FORMULA answer is
#     -- how the above are used in testing
#   THEN:
# CHANGE THE TO DO at the beginning of this comment to DONE.
# There is no code to be written for this TO DO (just reading).
# -----------------------------------------------------------------------------


def sum_from(m, n):
    total=0
    for k in range(n+1-m):
        total=total+(k+m)
    return total

    """
    What comes in:  The arguments are two integers m and n, with m <= n.
    What goes out:  Returns the sum of the integers from m to n,
      inclusive.
    Side effects:   None.
    Example:
        sum_from(6, 9) returns 6 + 7 + 8 + 9, that is, 30.
    """
    # -------------------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    #          Tests have been written for you (above).
    #
    # IMPORTANT:  Your solution MUST
    #   use an explicit    for ... in range(...):     statement
    #
    # IMPORTANT: As in previous problems in this session,
    #   you must NOT use the 2 or 3-parameter versions
    #   of the RANGE expression, if you happen to know them.
    # -------------------------------------------------------------------------


def run_test_factorial():
    """ Tests the   factorial   function. """
    # -------------------------------------------------------------------------
    # DONE: 4. Implement this TEST function.
    #   It TESTS the  factorial  function defined below.
    #   Include at least **   5   ** tests (we wrote two for you).
    #
    ###########################################################################
    # IMPORTANT: At least 2 of your tests MUST use the
    #    math.factorial
    # function as an ORACLE for testing.  See examples above.
    ###########################################################################
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   factorial   function:')
    print('--------------------------------------------------')

    # Test 1:
    answer_from_oracle = math.factorial(0)
    answer_from_my_code = factorial(0)
    print('Test 1 expected (from oracle):', answer_from_oracle)
    print('       actual (from my code): ', answer_from_my_code)

    # Test 2:
    answer_from_oracle = math.factorial(21)
    answer_from_my_code = factorial(21)
    print('Test 2 expected (from oracle):', answer_from_oracle)
    print('       actual (from my code): ', answer_from_my_code)

    # -------------------------------------------------------------------------
    # TO DO: 4 (continued).
    # Below this comment, add 3 more test cases, at least two of which
    #   ** uses  math.factorial  as an ORACLE for testing. **
    # -------------------------------------------------------------------------
    expected_3=3628800
    answer_3=factorial(10)
    print('Test 3 expected',expected_3)
    print('Test 3 actual',answer_3)
    expected_4=1307674368000
    answer_4=factorial(15)
    print('Test 4 expected',expected_4)
    print('Test 4 actual',answer_4)
    expected_5=402387260077093773543702433923003985719374864210714632543799910429938512398629020592044208486969404800479988610197196058631666872994808558901323829669944590997424504087073759918823627727188732519779505950995276120874975462497043601418278094646496291056393887437886487337119181045825783647849977012476632889835955735432513185323958463075557409114262417474349347553428646576611667797396668820291207379143853719588249808126867838374559731746136085379534524221586593201928090878297308431392844403281231558611036976801357304216168747609675871348312025478589320767169132448426236131412508780208000261683151027341827977704784635868170164365024153691398281264810213092761244896359928705114964975419909342221566832572080821333186116811553615836546984046708975602900950537616475847728421889679646244945160765353408198901385442487984959953319101723355556602139450399736280750137837615307127761926849034352625200015888535147331611702103968175921510907788019393178114194545257223865541461062892187960223838971476088506276862967146674697562911234082439208160153780889893964518263243671616762179168909779911903754031274622289988005195444414282012187361745992642956581746628302955570299024324153181617210465832036786906117260158783520751516284225540265170483304226143974286933061690897968482590125458327168226458066526769958652682272807075781391858178889652208164348344825993266043367660176999612831860788386150279465955131156552036093988180612138558600301435694527224206344631797460594682573103790084024432438465657245014402821885252470935190620929023136493273497565513958720559654228749774011413346962715422845862377387538230483865688976461927383814900140767310446640259899490222221765904339901886018566526485061799702356193897017860040811889729918311021171229845901641921068884387121855646124960798722908519296819372388642614839657382291123125024186649353143970137428531926649875337218940694281434118520158014123344828015051399694290153483077644569099073152433278288269864602789864321139083506217095002597389863554277196742822248757586765752344220207573630569498825087968928162753848863396909959826280956121450994871701244516461260379029309120889086942028510640182154399457156805941872748998094254742173582401063677404595741785160829230135358081840096996372524230560855903700624271243416909004153690105933983835777939410970027753472000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    answer_5=factorial(1000)
    print('Test 5 expected',expected_5)
    print('Test 5 actual',answer_5)
def factorial(n):
    total=1
    for k in range(n):
        total=total*(n-k)
    return total
    """
    What comes in:  The sole argument is a non-negative integer n.
    What goes out:  Returns n!, that is, n x (n-1) x (n-2) x ... x 1.
    Side effects:   None.
    Examples:
        factorial(5) returns 5 x 4 x 3 x 2 x 1, that is, 120.
        factorial(0) returns 1 (by definition).
    """
    # -------------------------------------------------------------------------
    # DONE: 5. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #
    # IMPORTANT:  Your solution MUST
    #   use an explicit    for ... in range(...):     statement.
    # -------------------------------------------------------------------------


def run_test_count_cosines_from():
    """ Tests the   count_cosines_from   function. """
    # -------------------------------------------------------------------------
    # DONE: 6. Implement this TEST function.
    #   It TESTS the  count_cosines_from  function defined below.
    #   Include at least **   6   ** tests (we wrote one for you).
    #              ** Yes, 6 (six) tests. **
    #     ** Counting problems are harder to test than summing. **
    #
    # To implement this TEST function, use the same 4 steps as before:
    #
    #   Step 1: Read the doc-string of  count_cosines_from  below.
    #     Understand what that function SHOULD return.
    #
    #   Step 2:  Pick a test case:  numbers that you could send as
    #     actual arguments to the  count_cosines_from  function.
    #
    #   Step 3: Figure out (by hand, or by using an oracle: a test case
    #     that your instructor provided in the doc-string, or a
    #     known formula or an alternative implementation that you trust)
    #     the CORRECT (EXPECTED) answer for your test case.
    #
    #   Step 4: Write code that prints both the EXPECTED answer
    #     and the ACTUAL answer returned when you call the function.
    #     Follow the same form as in the test case we provided below.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   count_cosines_from   function:')
    print('--------------------------------------------------')

    # Test 1:
    expected = 2
    answer = count_cosines_from(3, 9, 0.29)
    print('Test 1 expected:', expected)
    print('       actual:  ', answer)

    # -------------------------------------------------------------------------
    # TO DO: 6 (continued).
    # Below this comment, add 5 more test cases of your own choosing.
    # -------------------------------------------------------------------------
    answer_2=count_cosines_from(2,3,.3)
    expected_2=0
    print('Test 1 expected',expected_2)
    print('Test 1 actual',answer_2)
    answer_3=count_cosines_from(5,7,.5)
    expected_3=2
    print('Test 3 expected',expected_3)
    print('Test 3 actual',answer_3)
    answer_4=count_cosines_from(3,5,.2)
    expected_4=1
    print('Test 4 expected',expected_4)
    print('Test 4 actual',answer_4)
    answer_5=count_cosines_from(3,6,.3)
    expected_5=1
    print('Test 5 expected',expected_5)
    print('Test 5 actual',answer_5)

def count_cosines_from(m, n, x):
    count=0
    for k in range(n+1-m):
        if math.cos(m+k)>x:
            count=count+1
    return count
    """
    What comes in:  The three arguments are non-negative integers
      m and n, with m <= n, and a number x.
    What goes out:  Returns the number of integers from m to n,
      inclusive, whose cosine is greater than x.
    Side effects:   None.
    Examples:
    Since:  cosine(3) is about -0.99
            cosine(4) is about -0.65
            cosine(5) is about 0.28
            cosine(6) is about 0.96
            cosine(7) is about 0.75
            cosine(8) is about -0.15
            cosine(9) is about -0.91
      -- count_cosines_from(3, 9, 0.29)  returns  2
      -- count_cosines_from(3, 9, 0.27)  returns  3
      -- count_cosines_from(4, 8, -0.5)  returns  4
    """
    # -------------------------------------------------------------------------
    # DONE: 7. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #
    # IMPORTANT: As in previous problems in this session,
    #   you must NOT use the 2 or 3-parameter versions
    #   of the RANGE expression, if you happen to know them.
    # -------------------------------------------------------------------------


def run_test_sum_unit_fractions_from():
    """ Tests the   sum_unit_fractions_from   function. """
    # -------------------------------------------------------------------------
    # DONE: 8. Implement this TEST function.
    #   It TESTS the  sum_unit_fractions_from  function defined below.
    #   Include at least **   3   ** tests (we wrote one for you).
    # Use the same 4-step process as for previous TEST functions.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_unit_fractions_from   function:')
    print('--------------------------------------------------')

    # Test 1:
    expected = 0.545635  # This is APPROXIMATELY the correct answer.
    answer = sum_unit_fractions_from(6, 9)
    print('Test 1 expected:', expected, '(approximately)')
    print('       actual:  ', answer)

    # -------------------------------------------------------------------------
    # TO DO: 8 (continued).
    # Below this comment, add 2 more test cases of your own choosing.
    # -------------------------------------------------------------------------
    answer_2=sum_unit_fractions_from(7,10)
    expected_2=.4789682540
    print('Test 2 expected',expected_2)
    print('Test 2 actual',answer_2)
    answer_3=sum_unit_fractions_from(11,16)
    expected_3=.4517607393
    print('Test 3 expected',expected_3)
    print('Test 3 actual',answer_3)

def sum_unit_fractions_from(m, n):
    total=0
    for k in range(n+1-m):
       total=total+(1/(m+k))
    return total
    """
    What comes in:  Two positive integers m and n with m <= n.
    What goes out:  Returns the sum:
      1/m + 1/(m+1) + 1/(m+2) + ... + 1/n.
    Side effects:   None.
    Examples:
      -- sum_unit_fractions_from(6, 9) returns
            1/6 + 1/7 + 1/8 + 1/9
         which is about 0.545635
      -- sum_unit_fractions_from(10, 9000)  returns about  6.853
    """
    # -------------------------------------------------------------------------
    # DONE: 9. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #
    # IMPORTANT: As in previous problems in this session,
    #   you must NOT use the 2 or 3-parameter versions
    #   of the RANGE expression, if you happen to know them.
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
