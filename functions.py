from datetime import date
from re import template

TEST_NAMES = []
CURRENT_TEST_CASE_NAME = "X$$$NUMBER$$$"
TEST_COUNTER = 1


def generateHeaderName(filename):
    template = """/$$$STARS$$$/
/* Test Group(s) for $$$FILENAME$$$_Test */
/$$$STARS$$$/
    """
    template = template.replace("$$$FILENAME$$$", filename)
    template = template.replace("$$$STARS$$$", '*' * (len(filename) + 23 + 4))
    return template


def generateTestinTestGroup(filename):
    global TEST_COUNTER
    global TEST_NAMES

    template = """\\ref TEST($$$FILENAME$$$_Test, $$$FILENAME_UPERACSE$$$_$$$TEST_NO$$$)
    *             $$$TEST$$$"""
    template = template.replace("$$$FILENAME$$$", filename)
    template = template.replace("$$$FILENAME_UPERACSE$$$", filename.upper())
    template = template.replace(
        "$$$TEST_NO$$$",
        CURRENT_TEST_CASE_NAME.replace("$$$NUMBER$$$", str(TEST_COUNTER)))

    TEST_NAMES.append(
        CURRENT_TEST_CASE_NAME.replace("$$$NUMBER$$$", str(TEST_COUNTER)))
    TEST_COUNTER += 1
    return template


def generateTestGroup(filename, numberOfTests):
    template = """
TEST_GROUP($$$FILENAME$$$_Test)
{
    /**
    *   \section TestGroup
    *   \subsection $$$FILENAME$$$_Test
    *   - ***RETURN_TYPE*** $$$FILENAME$$$(***PARAMETERS***) \\n
    *   - Analysis of interface parameters and global data \\n
    *       - Input data \\ref  \\n
    *       - Parameter \\ref \\n
    *               
    *       - Control flow: test operation with code / branch coverage && Equivalence Partitioning and Boundary Test \\n
    *           actual test with line & branch coverage     =>  $$$NO_OF_TESTS$$$ TC  \\n
    *             $$$TEST$$$
    *
    *       - Global data: \\n
    *
    *   - TC_ASIL impact minimum $$$NO_OF_TESTS$$$ TC \\n
    */

    void setup()
    {
        
    }

    void teardown()
    {

    }
};
"""
    template = template.replace("$$$FILENAME$$$", filename)
    template = template.replace("$$$NO_OF_TESTS$$$", str(numberOfTests))
    for i in range(numberOfTests):
        template = template.replace("$$$TEST$$$",
                                    generateTestinTestGroup(filename))
    template = template.replace("$$$TEST$$$", " ")
    return template


def generateHeader(filename, username):
    template = """/*
 *  $$$FILENAME$$$_Test.cpp
 *
 *  Created on: $$$TODAY_DATE$$$
 *          Author: $$$USER$$$
 */
"""
    template = template.replace("$$$TODAY_DATE$$$",
                                date.today().strftime("%d.%m.%Y"))
    template = template.replace("$$$FILENAME$$$", filename)
    template = template.replace("$$$USER$$$", username)
    return template


def generateTestCases(filename):
    result = ""
    template = """
TEST($$$FILENAME$$$_Test, $$$FILENAME__UPERACSE$$$_$$$TEST_NO$$$)
{
    /**
    *   \section TestCases
    *   \subsection $$$FILENAME__UPERACSE$$$_$$$TEST_NO$$$
    *   - Purpose:  
    *   - Input:     
    *   - Return:   
    *   - Result:
    *              
    */

    /* expected mock calls */
   
    /* operation call */
  
    /* check results */
   
}"""
    for testName in TEST_NAMES:
        result += template.replace("$$$FILENAME$$$", filename).replace(
            "$$$FILENAME__UPERACSE$$$",
            filename.upper()).replace("$$$TEST_NO$$$", testName)
    result += "\n \n \n"
    return result
