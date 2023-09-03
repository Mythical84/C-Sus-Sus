grammar Csus;

options {
    language=Python3;
}

csus: (statement SEMI|bracket_statement)*;

statement: function | expr | string;

truth: boolean|conditional;

bracket_statement: label=('if'|'while') paren=parens brac=brackets;

function: name=('print'|'input'|'getPointer'|'addPointer'|'subPointer'|'createVar') paren=functioninput;

functioninput: '(' (statement ',')+ ')';

expr: '(' exp=expr ')'               # parenExpr
    | SUB exp=expr                   # NegExpr
    | lhs=expr op=(MUL|DIV) rhs=expr # OpExpr
    | lhs=expr op=(ADD|SUB) rhs=expr # OpExpr
    | atom=NUM                       # atomExpr
    ;

string: '"' STR '"';

parens: '(' t=truth ')';

brackets: '{' (statement SEMI)+ '}';

conditional: left=statement cond=('='|'~') right=statement;

boolean: ('true' | 'false');

STR: [a-zA-Z:]+;
NUM: [0-9]+;
SEMI: [;]+;
WS: [\r\n| ]+ -> skip;

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';