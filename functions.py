from datetime import date
from re import template

TEST_NAMES = []
CURRENT_TEST_CASE_NAME = "X$$$NUMBER$$$"
TEST_COUNTER = 1


def parseFilename(functionName):
    try:
        res = functionName.split(' ')[2].split('(')[0]
        return res
    except:
        return functionName


def generateHeaderName(functionName):
    functionName = parseFilename(functionName)
    template = """/$$$STARS$$$/
/* Test Group(s) for $$$FILENAME$$$_Test */
/$$$STARS$$$/
    """
    template = template.replace("$$$FILENAME$$$", functionName)
    template = template.replace("$$$STARS$$$",
                                '*' * (len(functionName) + 23 + 4))
    return template


def generateTestinTestGroup(functionName):
    functionName = parseFilename(functionName)
    global TEST_COUNTER
    global TEST_NAMES

    template = """\\ref TEST($$$FILENAME$$$_Test, $$$FILENAME_UPERACSE$$$_$$$TEST_NO$$$)
    *             $$$TEST$$$"""
    template = template.replace("$$$FILENAME$$$", functionName)
    template = template.replace("$$$FILENAME_UPERACSE$$$",
                                functionName.upper())
    template = template.replace(
        "$$$TEST_NO$$$",
        CURRENT_TEST_CASE_NAME.replace("$$$NUMBER$$$", str(TEST_COUNTER)))

    TEST_NAMES.append(
        CURRENT_TEST_CASE_NAME.replace("$$$NUMBER$$$", str(TEST_COUNTER)))
    TEST_COUNTER += 1
    return template


def generateTestGroup(functionName, numberOfTests):
    template = """
TEST_GROUP($$$FILENAME$$$_Test)
{
    /**
    *   \section TestGroup
    *   \subsection $$$FILENAME$$$_Test
    *   $$$FILENAME_W_ARGUMENTS$$$ \\n
    *   - Analysis of interface parameters and global data \\n
    *       - Global data \\ref  \\n
    *           => Nullpointer check for pointers (no additional TC) => 0 TC \\n
    *           => equivalence class test for enumerations (no additional TC) => 0 TC \\n	
    *           => range check for parameters that have defined ranges(no additional TC) => 0 TC \\n	
    *       
    *      - Parameter \\ref  \\n
    *           => Nullpointer check for pointers (no additional TC) => 0 TC \\n
    *           => equivalence class test for enumerations (no additional TC) => 3 TC \\n	
    *           => range check for parameters that have defined ranges(no additional TC) => 4 TC \\n
    *               
    *       - Control flow: test operation with code / branch coverage && Equivalence Partitioning and Boundary Test \\n
    *           actual test with line & branch coverage     =>  $$$NO_OF_TESTS$$$ TC  \\n
    *             $$$TEST$$$
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
    template = template.replace("$$$FILENAME$$$", parseFilename(functionName))
    template = template.replace("$$$FILENAME_W_ARGUMENTS$$$", functionName)
    functionName = parseFilename(functionName)
    template = template.replace("$$$NO_OF_TESTS$$$", str(numberOfTests))
    for i in range(numberOfTests):
        template = template.replace("$$$TEST$$$",
                                    generateTestinTestGroup(functionName))
    template = template.replace("$$$TEST$$$", " ")
    return template


def generateHeader(functionName, username):
    functionName = parseFilename(functionName)
    template = """/*
 *  $$$FILENAME$$$_Test.cpp
 *
 *  Created on: $$$TODAY_DATE$$$
 *          Author: $$$USER$$$
 */
"""
    template = template.replace("$$$TODAY_DATE$$$",
                                date.today().strftime("%d.%m.%Y"))
    template = template.replace("$$$FILENAME$$$", functionName)
    template = template.replace("$$$USER$$$", username)
    return template


def generateTestCases(functionName):
    functionName = parseFilename(functionName)
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
   
}\n\n"""
    for testName in TEST_NAMES:
        result += template.replace("$$$FILENAME$$$", functionName).replace(
            "$$$FILENAME__UPERACSE$$$",
            functionName.upper()).replace("$$$TEST_NO$$$", testName)
    result += "\n \n \n"
    return result


def cleanValues():
    global TEST_NAMES, CURRENT_TEST_CASE_NAME, TEST_COUNTER
    TEST_NAMES = []
    CURRENT_TEST_CASE_NAME = "X$$$NUMBER$$$"
    TEST_COUNTER = 1