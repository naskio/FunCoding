import requests


def format_code(src_code: str) -> str:
    res = requests.post(
        url="https://arlp8cgo97.execute-api.eu-west-1.amazonaws.com/fantomas-main-stage-1c52a6a/fantomas/preview/format",
        headers={
            'Content-Type': 'application/json',
        },
        json={
            "isFsi": False,
            "options": [
                {
                    "$type": "int",
                    "$value": [
                        0,
                        "IndentSize",
                        4
                    ]
                },
                {
                    "$type": "int",
                    "$value": [
                        1,
                        "MaxLineLength",
                        120
                    ]
                },
                {
                    "$type": "endOfLineStyle",
                    "$value": [
                        2,
                        "EndOfLine",
                        "lf"
                    ]
                },
                {
                    "$type": "bool",
                    "$value": [
                        3,
                        "InsertFinalNewline",
                        True
                    ]
                },
                {
                    "$type": "bool",
                    "$value": [
                        4,
                        "SpaceBeforeParameter",
                        True
                    ]
                },
                {
                    "$type": "bool",
                    "$value": [
                        5,
                        "SpaceBeforeLowercaseInvocation",
                        True
                    ]
                },
                {
                    "$type": "bool",
                    "$value": [
                        6,
                        "SpaceBeforeUppercaseInvocation",
                        False
                    ]
                },
                {
                    "$type": "bool",
                    "$value": [
                        7,
                        "SpaceBeforeClassConstructor",
                        False
                    ]
                },
                {
                    "$type": "bool",
                    "$value": [
                        8,
                        "SpaceBeforeMember",
                        False
                    ]
                },
                {
                    "$type": "bool",
                    "$value": [
                        9,
                        "SpaceBeforeColon",
                        False
                    ]
                },
                {
                    "$type": "bool",
                    "$value": [
                        10,
                        "SpaceAfterComma",
                        True
                    ]
                },
                {
                    "$type": "bool",
                    "$value": [
                        11,
                        "SpaceBeforeSemicolon",
                        False
                    ]
                },
                {
                    "$type": "bool",
                    "$value": [
                        12,
                        "SpaceAfterSemicolon",
                        True
                    ]
                },
                {
                    "$type": "bool",
                    "$value": [
                        13,
                        "SpaceAroundDelimiter",
                        True
                    ]
                },
                {
                    "$type": "int",
                    "$value": [
                        14,
                        "MaxIfThenElseShortWidth",
                        40
                    ]
                },
                {
                    "$type": "int",
                    "$value": [
                        15,
                        "MaxInfixOperatorExpression",
                        50
                    ]
                },
                {
                    "$type": "int",
                    "$value": [
                        16,
                        "MaxRecordWidth",
                        40
                    ]
                },
                {
                    "$type": "int",
                    "$value": [
                        17,
                        "MaxRecordNumberOfItems",
                        1
                    ]
                },
                {
                    "$type": "multilineFormatterType",
                    "$value": [
                        18,
                        "RecordMultilineFormatter",
                        "character_width"
                    ]
                },
                {
                    "$type": "int",
                    "$value": [
                        19,
                        "MaxArrayOrListWidth",
                        40
                    ]
                },
                {
                    "$type": "int",
                    "$value": [
                        20,
                        "MaxArrayOrListNumberOfItems",
                        1
                    ]
                },
                {
                    "$type": "multilineFormatterType",
                    "$value": [
                        21,
                        "ArrayOrListMultilineFormatter",
                        "character_width"
                    ]
                },
                {
                    "$type": "int",
                    "$value": [
                        22,
                        "MaxValueBindingWidth",
                        80
                    ]
                },
                {
                    "$type": "int",
                    "$value": [
                        23,
                        "MaxFunctionBindingWidth",
                        40
                    ]
                },
                {
                    "$type": "int",
                    "$value": [
                        24,
                        "MaxDotGetExpressionWidth",
                        50
                    ]
                },
                {
                    "$type": "bool",
                    "$value": [
                        25,
                        "MultilineBlockBracketsOnSameColumn",
                        False
                    ]
                },
                {
                    "$type": "bool",
                    "$value": [
                        26,
                        "NewlineBetweenTypeDefinitionAndMembers",
                        False
                    ]
                },
                {
                    "$type": "bool",
                    "$value": [
                        27,
                        "AlignFunctionSignatureToIndentation",
                        False
                    ]
                },
                {
                    "$type": "bool",
                    "$value": [
                        28,
                        "AlternativeLongMemberDefinitions",
                        False
                    ]
                },
                {
                    "$type": "bool",
                    "$value": [
                        29,
                        "MultiLineLambdaClosingNewline",
                        False
                    ]
                },
                {
                    "$type": "bool",
                    "$value": [
                        30,
                        "ExperimentalKeepIndentInBranch",
                        False
                    ]
                },
                {
                    "$type": "bool",
                    "$value": [
                        31,
                        "BlankLinesAroundNestedMultilineExpressions",
                        True
                    ]
                },
                {
                    "$type": "bool",
                    "$value": [
                        32,
                        "BarBeforeDiscriminatedUnionDeclaration",
                        False
                    ]
                },
                {
                    "$type": "bool",
                    "$value": [
                        33,
                        "ExperimentalStroustrupStyle",
                        False
                    ]
                },
                {
                    "$type": "int",
                    "$value": [
                        34,
                        "KeepMaxNumberOfBlankLines",
                        100
                    ]
                },
                {
                    "$type": "bool",
                    "$value": [
                        35,
                        "StrictMode",
                        False
                    ]
                }
            ],
            "sourceCode": src_code,
        })
    res.raise_for_status()
    return res.json().get('firstFormat')  # firstFormat, secondFormat, firstValidation, secondValidation
