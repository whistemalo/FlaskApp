from flask import Flask, render_template, url_for, request
import pandas as pd
import numpy as np
import mysql.connector
from enum import Enum
from enum import auto

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")

 
# def pruebas (output):
#     funcion_dentro_funcion(output)
#     print("llega a la funcion")

# def funcion_dentro_funcion(output):
#     print('<<<<<<-----------------funcion dentro de otra funcion fucniona!!! -------------->>>')
#     print(output)


def parser(sql_sentence_web):
    import pandas as pd
    import numpy as np
    import mysql.connector
    def new_trie(keywords):
        trie = {}

        for key in keywords:
            current = trie

            for char in key:
                current = current.setdefault(char, {})
            current[0] = True

        return trie


    def in_trie(trie, key):
        if not key:
            return 0

        current = trie

        for char in key:
            if char not in current:
                return 0
            current = current[char]

        if 0 in current:
            return 2
        return 1

    from enum import Enum

    class AutoName(Enum):
        # pylint: disable=no-self-argument
        def _generate_next_value_(name, _start, _count, _last_values):
            return name

    def ensure_list(value):
        if value is None:
            return []
        return value if isinstance(value, (list, set)) else [value]


    def list_get(arr, index):
        try:
            return arr[index]
        except IndexError:
            return None

    from enum import auto

    class ErrorLevel(AutoName):
        IGNORE = auto()
        WARN = auto()
        RAISE = auto()


    class UnsupportedError(ValueError):
        pass


    class ParseError(ValueError):
        pass


    class TokenError(ValueError):
        pass

    #**************************-------------------------------adas
    # add_cascade(label="sa
    # da
    # sd
    # asd
    # as
    # d
    # as
    # ", menu=)

    from enum import auto
    class TokenType(AutoName):
        L_PAREN = auto()
        R_PAREN = auto()
        L_BRACKET = auto()
        R_BRACKET = auto()
        L_BRACE = auto()
        R_BRACE = auto()
        COMMA = auto()
        DOT = auto()
        DASH = auto()
        PLUS = auto()
        COLON = auto()
        DCOLON = auto()
        SEMICOLON = auto()
        STAR = auto()
        SLASH = auto()
        LT = auto()
        LTE = auto()
        GT = auto()
        GTE = auto()
        NOT = auto()
        EQ = auto()
        NEQ = auto()
        AND = auto()
        OR = auto()
        AMP = auto()
        DPIPE = auto()
        PIPE = auto()
        CARET = auto()
        TILDA = auto()
        LSHIFT = auto()
        RSHIFT = auto()
        LAMBDA = auto()

        SPACE = auto()
        BREAK = auto()

        STRING = auto()
        NUMBER = auto()
        IDENTIFIER = auto()
        COLUMN = auto()
        COLUMN_DEF = auto()
        SCHEMA = auto()
        TABLE = auto()
        VAR = auto()

        # types
        BOOLEAN = auto()
        TINYINT = auto()
        SMALLINT = auto()
        INT = auto()
        BIGINT = auto()
        FLOAT = auto()
        DOUBLE = auto()
        DECIMAL = auto()
        CHAR = auto()
        VARCHAR = auto()
        TEXT = auto()
        BINARY = auto()
        JSON = auto()
        TIMESTAMP = auto()
        TIMESTAMPTZ = auto()
        DATE = auto()

        # keywords
        ADD_FILE = auto()
        ALIAS = auto()
        ALL = auto()
        ALTER = auto()
        ARRAY = auto()
        ASC = auto()
        AUTO_INCREMENT = auto()
        BETWEEN = auto()
        BUCKET = auto()
        BY = auto()
        CACHE = auto()
        CASE = auto()
        CAST = auto()
        CHARACTER_SET = auto()
        COUNT = auto()
        COLLATE = auto()
        COMMENT = auto()
        COMMENT_END = auto()
        COMMENT_START = auto()
        CREATE = auto()
        CROSS = auto()
        CURRENT_ROW = auto()
        DATABASE = auto()
        DIV = auto()
        DEFAULT = auto()
        DELETE = auto()
        DESC = auto()
        DISTINCT = auto()
        DROP = auto()
        ELSE = auto()
        END = auto()
        ENGINE = auto()
        EXCEPT = auto()
        EXISTS = auto()
        EXPLAIN = auto()
        EXTRACT = auto()
        FOLLOWING = auto()
        FORMAT = auto()
        FULL = auto()
        FROM = auto()
        GROUP = auto()
        HAVING = auto()
        HINT = auto()
        IF = auto()
        IN = auto()
        INNER = auto()
        INSERT = auto()
        INTERSECT = auto()
        INTERVAL = auto()
        INTO = auto()
        IS = auto()
        JOIN = auto()
        LATERAL = auto()
        LAZY = auto()
        LEFT = auto()
        LIKE = auto()
        LIMIT = auto()
        MAP = auto()
        MOD = auto()
        NULL = auto()
        ON = auto()
        OPTIONS = auto()
        ORDER = auto()
        ORDERED = auto()
        ORDINALITY = auto()
        OUTER = auto()
        OUT_OF = auto()
        OVER = auto()
        OVERWRITE = auto()
        PARTITION = auto()
        PERCENT = auto()
        PRECEDING = auto()
        PRIMARY_KEY = auto()
        RANGE = auto()
        RECURSIVE = auto()
        REPLACE = auto()
        RIGHT = auto()
        RLIKE = auto()
        ROWS = auto()
        SCHEMA_COMMENT = auto()
        SELECT = auto()
        SET = auto()
        SHOW = auto()
        STORED = auto()
        TABLE_SAMPLE = auto()
        TEMPORARY = auto()
        TIME = auto()
        THEN = auto()
        UNBOUNDED = auto()
        UNION = auto()
        UNNEST = auto()
        UPDATE = auto()
        VALUES = auto()
        VIEW = auto()
        WHEN = auto()
        WHERE = auto()
        WITH = auto()
        WITHOUT = auto()
        ZONE = auto()


    class Token:
        __slots__ = ("token_type", "text", "line", "col")

        @classmethod
        def number(cls, number):
            return cls(TokenType.NUMBER, str(number))

        @classmethod
        def string(cls, string):
            return cls(TokenType.STRING, string)

        @classmethod
        def identifier(cls, identifier):
            return cls(TokenType.IDENTIFIER, identifier)

        @classmethod
        def var(cls, var):
            return cls(TokenType.VAR, var)

        def __init__(self, token_type, text, line=1, col=1):
            self.token_type = token_type
            self.text = text
            self.line = line
            self.col = max(col - len(text), 1)

        def __repr__(self):
            attributes = ", ".join(f"{k}: {getattr(self, k)}" for k in self.__slots__)
            return f"<Token {attributes}>"


    def new_ambiguous(keywords, single_tokens):
        return new_trie(
            key
            for key, value in keywords.items()
            if value not in (TokenType.COMMENT, TokenType.COMMENT_START)
            and (" " in key or any(single in key for single in single_tokens))
        )


    class Tokenizer:
        SINGLE_TOKENS = {
            "(": TokenType.L_PAREN,
            ")": TokenType.R_PAREN,
            "[": TokenType.L_BRACKET,
            "]": TokenType.R_BRACKET,
            "{": TokenType.L_BRACE,
            "}": TokenType.R_BRACE,
            "&": TokenType.AMP,
            "^": TokenType.CARET,
            ":": TokenType.COLON,
            ",": TokenType.COMMA,
            ".": TokenType.DOT,
            "-": TokenType.DASH,
            "=": TokenType.EQ,
            ">": TokenType.GT,
            "<": TokenType.LT,
            "%": TokenType.MOD,
            "!": TokenType.NOT,
            "|": TokenType.PIPE,
            "+": TokenType.PLUS,
            ";": TokenType.SEMICOLON,
            "/": TokenType.SLASH,
            "*": TokenType.STAR,
            "~": TokenType.TILDA,
        }

        KEYWORDS = {
            "/*+": TokenType.HINT,
            "--": TokenType.COMMENT,
            "/*": TokenType.COMMENT_START,
            "*/": TokenType.COMMENT_END,
            "==": TokenType.EQ,
            "::": TokenType.DCOLON,
            "||": TokenType.DPIPE,
            ">=": TokenType.GTE,
            "<=": TokenType.LTE,
            "<>": TokenType.NEQ,
            "!=": TokenType.NEQ,
            "<<": TokenType.LSHIFT,
            ">>": TokenType.RSHIFT,
            "->": TokenType.LAMBDA,
            "ADD ARCHIVE": TokenType.ADD_FILE,
            "ADD ARCHIVES": TokenType.ADD_FILE,
            "ADD FILE": TokenType.ADD_FILE,
            "ADD FILES": TokenType.ADD_FILE,
            "ADD JAR": TokenType.ADD_FILE,
            "ADD JARS": TokenType.ADD_FILE,
            "ALL": TokenType.ALL,
            "ALTER": TokenType.ALTER,
            "AND": TokenType.AND,
            "ASC": TokenType.ASC,
            "AS": TokenType.ALIAS,
            "AUTO_INCREMENT": TokenType.AUTO_INCREMENT,
            "BETWEEN": TokenType.BETWEEN,
            "BUCKET": TokenType.BUCKET,
            "BY": TokenType.BY,
            "CACHE": TokenType.CACHE,
            "CASE": TokenType.CASE,
            "CAST": TokenType.CAST,
            "CHARACTER SET": TokenType.CHARACTER_SET,
            "COLLATE": TokenType.COLLATE,
            "COMMENT": TokenType.SCHEMA_COMMENT,
            "COUNT": TokenType.COUNT,
            "CREATE": TokenType.CREATE,
            "CROSS": TokenType.CROSS,
            "CURRENT ROW": TokenType.CURRENT_ROW,
            "DATABASE": TokenType.DATABASE,
            "DIV": TokenType.DIV,
            "DEFAULT": TokenType.DEFAULT,
            "DELETE": TokenType.DELETE,
            "DESC": TokenType.DESC,
            "DISTINCT": TokenType.DISTINCT,
            "DROP": TokenType.DROP,
            "ELSE": TokenType.ELSE,
            "END": TokenType.END,
            "ENGINE": TokenType.ENGINE,
            "EXCEPT": TokenType.EXCEPT,
            "EXISTS": TokenType.EXISTS,
            "EXPLAIN": TokenType.EXPLAIN,
            "EXTRACT": TokenType.EXTRACT,
            "FORMAT": TokenType.FORMAT,
            "FULL": TokenType.FULL,
            "FOLLOWING": TokenType.FOLLOWING,
            "FROM": TokenType.FROM,
            "GROUP BY": TokenType.GROUP,
            "HAVING": TokenType.HAVING,
            "IF": TokenType.IF,
            "IN": TokenType.IN,
            "INNER": TokenType.INNER,
            "INSERT": TokenType.INSERT,
            "INTERVAL": TokenType.INTERVAL,
            "INTERSECT": TokenType.INTERSECT,
            "INTO": TokenType.INTO,
            "IS": TokenType.IS,
            "JOIN": TokenType.JOIN,
            "LATERAL": TokenType.LATERAL,
            "LAZY": TokenType.LAZY,
            "LEFT": TokenType.LEFT,
            "LIKE": TokenType.LIKE,
            "LIMIT": TokenType.LIMIT,
            "NOT": TokenType.NOT,
            "NULL": TokenType.NULL,
            "ON": TokenType.ON,
            "OPTIONS": TokenType.OPTIONS,
            "OR": TokenType.OR,
            "ORDER BY": TokenType.ORDER,
            "ORDINALITY": TokenType.ORDINALITY,
            "OUTER": TokenType.OUTER,
            "OUT OF": TokenType.OUT_OF,
            "OVER": TokenType.OVER,
            "OVERWRITE": TokenType.OVERWRITE,
            "PARTITION BY": TokenType.PARTITION,
            "PERCENT": TokenType.PERCENT,
            "PRECEDING": TokenType.PRECEDING,
            "PRIMARY KEY": TokenType.PRIMARY_KEY,
            "RANGE": TokenType.RANGE,
            "RECURSIVE": TokenType.RECURSIVE,
            "REGEXP": TokenType.RLIKE,
            "REPLACE": TokenType.REPLACE,
            "RIGHT": TokenType.RIGHT,
            "RLIKE": TokenType.RLIKE,
            "ROWS": TokenType.ROWS,
            "SELECT": TokenType.SELECT,
            "SET": TokenType.SET,
            "SHOW": TokenType.SHOW,
            "STORED": TokenType.STORED,
            "TABLE": TokenType.TABLE,
            "TABLESAMPLE": TokenType.TABLE_SAMPLE,
            "TEMP": TokenType.TEMPORARY,
            "TEMPORARY": TokenType.TEMPORARY,
            "THEN": TokenType.THEN,
            "TIME": TokenType.TIME,
            "UNBOUNDED": TokenType.UNBOUNDED,
            "UNION": TokenType.UNION,
            "UNNEST": TokenType.UNNEST,
            "UPDATE": TokenType.UPDATE,
            "VALUES": TokenType.VALUES,
            "VIEW": TokenType.VIEW,
            "WHEN": TokenType.WHEN,
            "WHERE": TokenType.WHERE,
            "WITH": TokenType.WITH,
            "WITHOUT": TokenType.WITHOUT,
            "ZONE": TokenType.ZONE,
            "ARRAY": TokenType.ARRAY,
            "BOOL": TokenType.BOOLEAN,
            "BOOLEAN": TokenType.BOOLEAN,
            "BYTE": TokenType.TINYINT,
            "TINYINT": TokenType.TINYINT,
            "SHORT": TokenType.SMALLINT,
            "SMALLINT": TokenType.SMALLINT,
            "INT2": TokenType.SMALLINT,
            "INTEGER": TokenType.INT,
            "INT": TokenType.INT,
            "INT4": TokenType.INT,
            "LONG": TokenType.BIGINT,
            "BIGINT": TokenType.BIGINT,
            "INT8": TokenType.BIGINT,
            "DECIMAL": TokenType.DECIMAL,
            "MAP": TokenType.MAP,
            "NUMERIC": TokenType.DECIMAL,
            "FIXED": TokenType.DECIMAL,
            "REAL": TokenType.FLOAT,
            "FLOAT": TokenType.FLOAT,
            "FLOAT4": TokenType.FLOAT,
            "FLOAT8": TokenType.DOUBLE,
            "DOUBLE": TokenType.DOUBLE,
            "JSON": TokenType.JSON,
            "CHAR": TokenType.CHAR,
            "VARCHAR": TokenType.VARCHAR,
            "STRING": TokenType.TEXT,
            "TEXT": TokenType.TEXT,
            "BINARY": TokenType.BINARY,
            "TIMESTAMP": TokenType.TIMESTAMP,
            "TIMESTAMPTZ": TokenType.TIMESTAMPTZ,
            "DATE": TokenType.DATE,
        }

        WHITE_SPACE = {
            " ": TokenType.SPACE,
            "\t": TokenType.SPACE,
            "\n": TokenType.BREAK,
            "\r": TokenType.BREAK,
            "\rn": TokenType.BREAK,
        }

        COMMANDS = {
            TokenType.ALTER,
            TokenType.ADD_FILE,
            TokenType.DELETE,
            TokenType.EXPLAIN,
            TokenType.SET,
            TokenType.SHOW,
        }

        ESCAPE_CODE = "__sqlglot_escape__"

        AMBIGUOUS = new_ambiguous(KEYWORDS, SINGLE_TOKENS)
        COMMENTS = ["--"]
        COMMENT_START = "/*"
        COMMENT_END = "*/"

        __slots__ = (
            "quotes",
            "identifier",
            "escape",
            "code",
            "size",
            "tokens",
            "_start",
            "_current",
            "_line",
            "_col",
            "_char",
            "_end",
            "_peek",
            "__text",
        )

        def __init__(self, quotes=None, identifier=None, escape=None):
            self.quotes = set(ensure_list(quotes) or ["'"])
            self.identifier = identifier or '"'
            self.escape = escape or "'"
            self.reset()

        def reset(self):
            self.code = ""
            self.size = 0
            self.tokens = []
            self._start = 0
            self._current = 0
            self._line = 1
            self._col = 1

            self._char = None
            self._end = None
            self._peek = None
            self.__text = None

        def tokenize(self, code):  # pylint: disable=too-many-branches
            self.reset()
            self.code = code
            self.size = len(code)

            while not self._end:
                self._start = self._current
                self._advance()

                if not self._char:
                    break
                if self._scan_ambiguous():
                    pass
                elif self._scan_comments():
                    pass
                elif self._char in self.SINGLE_TOKENS:
                    self._add(self.SINGLE_TOKENS[self._char])
                elif self._char in self.WHITE_SPACE:
                    white_space = self.WHITE_SPACE[self._char]
                    if white_space == TokenType.BREAK:
                        self._col = 1
                        self._line += 1
                elif self._char.isdigit():
                    self._scan_number()
                elif self._char in self.quotes:
                    self._scan_string()
                elif self._char == self.identifier:
                    self._scan_identifier()
                else:
                    self._scan_var()

            return self.tokens

        def _chars(self, size):
            start = self._current - 1
            end = start + size
            if end <= self.size:
                return self.code[start:end].upper()
            return ""

        def _advance(self, i=1):
            self._col += i
            self._current += i
            self._char = list_get(self.code, self._current - 1)
            self._peek = list_get(self.code, self._current) or ""
            self._end = self._current >= self.size
            self.__text = None

        @property
        def _text(self):
            if self.__text is None:
                self.__text = self.code[self._start : self._current]
            return self.__text

        def _add(self, token_type, text=None):
            text = self._text if text is None else text
            self.tokens.append(Token(token_type, text, self._line, self._col))

            if token_type in self.COMMANDS and (
                len(self.tokens) == 1 or self.tokens[-2].token_type == TokenType.SEMICOLON
            ):
                self._start = self._current
                while not self._end and self._peek != ";":
                    self._advance()
                if self._start < self._current:
                    self._add(TokenType.STRING)

        def _scan_ambiguous(self):
            size = 1
            word = None
            chars = self._chars(size)

            while chars:
                result = in_trie(self.AMBIGUOUS, chars)

                if result == 0:
                    break
                if result == 2:
                    word = chars
                size += 1
                chars = self._chars(size)

            if word:
                self._advance(len(word) - 1)
                self._add(self.KEYWORDS[word])
                return True
            return False

        def _scan_comments(self):
            for comment in self.COMMENTS:
                if self._chars(len(comment)) == comment:
                    while (
                        not self._end
                        and self.WHITE_SPACE.get(self._char) != TokenType.BREAK
                    ):
                        self._advance()
                    return True

            if self._chars(len(self.COMMENT_START)) == self.COMMENT_START:
                comment_end_size = len(self.COMMENT_END)
                while not self._end and self._chars(comment_end_size) != self.COMMENT_END:
                    self._advance()
                self._advance(comment_end_size - 1)
                return True
            return False

        def _scan_number(self):
            decimal = False
            scientific = 0

            while True:
                if self._peek.isdigit():
                    self._advance()
                elif self._peek == "." and not decimal:
                    decimal = True
                    self._advance()
                elif self._peek.upper() == "E" and not scientific:
                    scientific += 1
                    self._advance()
                elif self._peek == "-" and scientific == 1:
                    scientific += 1
                    self._advance()
                else:
                    return self._add(TokenType.NUMBER)

        def _scan_string(self):
            text = []
            quote = self._char

            while True:
                if self._end:
                    raise RuntimeError(f"Missing {quote} from {self._line}:{self._start}")
                text.append(self._char)
                self._advance()

                if self._char == self.escape and self._peek == quote:
                    text.append(self.ESCAPE_CODE)
                    self._advance()
                elif self._char == quote:
                    break
                elif self._char == "'":
                    text.append(self.ESCAPE_CODE)

            text.append(self._char)
            self._add(TokenType.STRING, "".join(text[1:-1]))

        def _scan_identifier(self):
            while self._peek != self.identifier:
                if self._end:
                    raise RuntimeError(
                        f"Missing {self.identifier} from {self._line}:{self._start}"
                    )
                self._advance()
            self._advance()
            self._add(TokenType.IDENTIFIER, self._text[1:-1])

        def _scan_var(self):
            while True:
                char = self._peek.strip()
                if char and char not in self.SINGLE_TOKENS:
                    self._advance()
                else:
                    break
            self._add(self.KEYWORDS.get(self._text.upper(), TokenType.VAR))

    #funciones
    def syntaxError(target):
        print("Error en la syntaxis: ",target)

    def get_dblist(dbName):
        conn = mysql.connector.connect (user='root', password='12345',
                                host='localhost',buffered=True)
        cursor = conn.cursor()
        exist=False
        listdb=[]
        databases = ("SHOW DATABASES")
        cursor.execute(databases)
        for (databases) in cursor:
            listdb.append(databases[0]);
        conn.close()
        for x in listdb:
            if x == dbName.lower(): 
                exist=True
        return exist

    def get_table_list(dbname, tableName):
        
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database=dbname)

        mycursor = mydb.cursor()
        mycursor.execute("SHOW TABLES")
        

        for x in mycursor:
            if x[0]== str(tableName.lower()):
                mydb.close()
                return True
        mydb.close()
        return False

    def create_db(query):
        querybuild=" ".join(map(str,query))
        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="12345"
                )
        mycursor = mydb.cursor()
        mycursor.execute(querybuild)
        mycursor.close()

    def execute_query(query,dbname):
        querybuild=""" """
        for x in range (len(query)):
            if tokens_arr[x]=='STRING':
                querybuild=querybuild+'"'+query[x]+'"'
            else:
                querybuild=querybuild+' '+query[x]
        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="12345",
                database=dbname
                )

        if mydb.is_connected()==False:
            print("No esta conectado")
        elif mydb.is_connected()==True:
            print("Conectado")

        mycursor = mydb.cursor()
        mycursor.execute(str(querybuild))
        mydb.commit()
        print(mycursor.rowcount, "datos ingresados.")
        mydb.close()
        return 

    def create_table_analisis_apend(tokens_query, text_query,i):
        if tokens_query[i]=='L_PAREN':
            i+=1
            if tokens_query[i]== 'NUMBER':
                i+=1
                if tokens_query[i] == 'R_PAREN' and tokens_query[i+1]=='COMMA':
                    i+=1
                elif tokens_query[i] == 'R_PAREN' and tokens_query[i] == 'R_PAREN' and tokens_query[i+2]=='SEMICOLON':
                    return len(tokens_query)
                else:
                    print("falta una coma ", text_query[i-3],text_query[i-2],text_query[i-1],text_query[i], ',')
                    return len(tokens_query) 
        return i
        
    def create_table_analisis(tokens_query, text_query):
        i=3
        if tokens_query[i]=="L_PAREN":
            while i< len(tokens_query):
                i+=1
                if tokens_query[i] == "VAR":
                    i+=1
                    #varchar
                    if tokens_query[i]=='VARCHAR':
                        i+=1
                        i=create_table_analisis_apend(tokens_query, text_query,i)
                    #var
                    elif tokens_query[i]=='CHAR':
                        i+=1
                        i=create_table_analisis_apend(tokens_query, text_query,i)
                    #int
                    elif tokens_query[i]=='INT':
                        i+=1
                        i=create_table_analisis_apend(tokens_query, text_query,i)

                    #float
                    elif tokens_query[i]=='INT':
                        i+=1
                        i=create_table_analisis_apend(tokens_query, text_query,i)

                    #DATE
                    elif tokens_query[i]=='DATE':
                        i+=1
                        if tokens_query[i] == 'R_PAREN' and tokens_query[i+1]=='COMMA':
                            i+=1
                        elif tokens_query[i] == 'R_PAREN' and tokens_query[i+1]=='SEMICOLON':
                            return True
                            
                        elif tokens_query[i]=='COMMA':
                            return True 
                        else:
                            print("falta una coma ", text_query[i-1],text_query[i], ',')
                            return False
                else:
                    syntaxError(text_query[i-1])
                    return False   
        else:
            print('Sintax error se esperaba un "(" luego de ', text_query[i-1])
            return False
            
        return True

    # INSERT INTO ruby (col1,col2) VALUES(col2*2,15);

    def insert_analisis(tokens_query, text_query,x):
        if tokens_query[x+1]=='L_PAREN':
            x+=2
            while x < len(tokens_query)-1:
                if tokens_query[x]=="STRING" or tokens_query[x]=="NUMBER" and tokens_query[x+1]=="COMMA":
                    x+=2
                elif tokens_query[x] == 'NUMBER' or tokens_query[x] == 'STRING':
                    x+=1
                    try:
                        if tokens_query[x]=='R_PAREN' and tokens_query[x+1]=='SEMICOLON':
                            return True
                        else:
                            print('error sintactico')
                            return False
                    except IndexError:
                        print("Falta ';'" )
                        return False
                    
                else:
                    print("Error de sintaxis: ",text_query[x],text_query[x+1] ) 
                    return False
        else:
            print('Error de sintaxis: ',text_query[x],'"',text_query[x+1],'"') 
            return False
        return True

    def get_table_columns(dbname,campos,tb_name):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345",
            database=dbname)

        if mydb.is_connected()==False:
            print("No esta conectado")
        elif mydb.is_connected()==True:
            print("Conexion exitosa")

        mycursor = mydb.cursor()
        query="SELECT * FROM " + tb_name
        mycursor.execute(query)
        existen=0
        for x in (mycursor.description):
            for y in campos:
                if y==x[0]:
                    existen+=1
                    print('Columna ', x[0],' existe')
                    
        if existen != len(campos):
            print('algunas columnas no existen')
            return False
    
        return True
    


    def parserProcess(tokens_arr,tokens_text_arr):
        dbname='baseprueba'
        if tokens_arr[0]=='CREATE' and  tokens_arr[1]=='DATABASE':
            try:
                tokens_text_arr[2]
                
                if get_dblist(tokens_text_arr[2])==True:
                    return("La base de datos ya existe")
                else:
                    try:
                        
                        if  tokens_arr[2]=='VAR':
                            dbname=tokens_text_arr[2]
                            create_db(tokens_text_arr)
                            print('Base de datos "', tokens_text_arr[2] ,'" ha sido creada exitosamente')
                        else:
                            syntaxError(tokens_text_arr[2])
                    except NameError:
                        print("Error en la sitaxis")
                        pass
            except IndexError:
                print("Error en la sytaxis: ", " ".join(map(str,tokens_text_arr)))
                
        #Basico verificacion de la sentencia Drop database            
        elif tokens_arr[0]=='DROP' and  tokens_arr[1]=='DATABASE':
            try:
                tokens_text_arr[2]
                if get_dblist(tokens_text_arr[2])==True:
                    try:
                        execute_query(tokens_text_arr,dbname)
                        print('Base de datos "', tokens_text_arr[2] ,'" ha sido eliminiada exitosamente')
                    except NameError:
                        print("Error en la sitaxis")
                        pass
                else:
                    print("La base de datos NO existe")

            except IndexError:
                print("Error en la sytaxis: ", " ".join(map(str,tokens_text_arr)))

        #create table
        elif tokens_arr[0]=='CREATE' and  tokens_arr[1]=='TABLE':
            try:

                if tokens_arr[2]=="VAR":
                    # validadacion de los parentesis
                    Par=0
                    for x in tokens_text_arr:
                        if x == "(":
                            Par=Par+1
                        elif x == ")":
                            Par=Par-1
                    if Par==0:
                        if create_table_analisis(tokens_arr, tokens_text_arr)==True:
                            if get_table_list(dbname, tokens_text_arr[2])==False:
                                execute_query(tokens_text_arr,dbname)
                                print('Tabla "{}" creada exitosamente'.format(tokens_text_arr[2]))
                            else:
                                print('La tabla "{}" ya existe'.format(tokens_text_arr[2]))
                        else:
                            syntaxError((" ".join(map(str,tokens_text_arr))))
                    else:   
                        print("Error de sintaxis quizas falta un '(' ó ')'?")   
                else:
                    print("Nombre de la tabla invalido")         

            except IndexError:
                print("Error en la sytaxis: ", " ".join(map(str,tokens_text_arr)))

        #drop table           
        elif tokens_arr[0]=='DROP' and  tokens_arr[1]=='TABLE':
            try:
                tokens_text_arr[2]
                
                if get_table_list(dbname, tokens_text_arr[2])==True:
                    try:
                        execute_query(tokens_text_arr,dbname)
                        print('Tabla "', tokens_text_arr[2] ,'" ha sido eliminiada exitosamente')
                    except NameError:
                        print("Error en la sitaxis")
                        pass
                else:
                    print("La tabla NO existe 2")

            except IndexError:
                print("Error en la sytaxis: ", " ".join(map(str,tokens_text_arr)))

        #insert
        elif tokens_arr[0]=='INSERT' and tokens_arr[1]=='INTO':
            if get_table_list(dbname,tokens_text_arr[2])==True:

                if tokens_arr[2]=='VAR' and tokens_arr[3]=='L_PAREN':
                    Parentesis=0 #contador de parenteis, si un parentesis se habre se tiene que cerrar
                    campos=[] #guarda nombres de columnas ejemplo "col1,col2"
                    values=False #bool que se encarga de verificar que Values exista en al sentencia
                    for x in range (len(tokens_arr)):
                            
                        if tokens_arr[x] == "L_PAREN":
                            Parentesis+=1
                        elif tokens_arr[x]=='VAR':
                                if tokens_arr[x+1]=='COMMA' or tokens_arr[x+1]=='R_PAREN':
                                    campos.append(tokens_text_arr[x])
                                elif tokens_arr[x+1]=='L_PAREN':
                                    print('')
                                else:
                                    print('Error: ',tokens_text_arr[x-1],tokens_text_arr[x],tokens_text_arr[x+1])
                        elif tokens_arr[x] == "R_PAREN":
                            Parentesis-=1
                        elif tokens_arr[x] == "VALUES" and Parentesis!=0:
                            print('Syntax error: ',tokens_text_arr[x-1], "')'",tokens_text_arr[x])
                        elif tokens_arr[x] == "VALUES":
                            values=True
                            break
                    if Parentesis==0 and values==True and get_table_columns(dbname,campos,tokens_text_arr[2])==True:
                        if insert_analisis(tokens_arr,tokens_text_arr,x) == True:
                            execute_query(tokens_text_arr,dbname)
            else:
                print('La tabla {} no existe'.format(tokens_text_arr[2]))
        else:
            target=str(tokens_text_arr[0])+ ' ' + str(tokens_text_arr[1]) + ' ' + str(tokens_text_arr[3])
            syntaxError(target)


    tokens = Tokenizer().tokenize(sql_sentence_web)
    tokens_arr=[]
    tokens_text_arr=[]
    dataTest=tokens
    for x in range(len(tokens)):
        var=tokens[x]
        tokens_arr.append(str(var.token_type).removeprefix("TokenType."))
        tokens_text_arr.append(str(var.text))
    print(tokens_arr)
    print(tokens_text_arr)
    
    
    return parserProcess(tokens_arr,tokens_text_arr)


########################################################
########################################################
########################################################
########################################################
########################################################



@app.route('/result',methods=['POST', 'GET'])
def result():
    output = request.form.to_dict()
    print("pruebas",output)
    name = (parser(output["name"]))
    
    # name = output["name"]


    return render_template('index.html', name = name)
    

if __name__ == "__main__":
    app.run(debug=True)

