from enum import IntEnum, auto
import judge0

from server.domain.entities.base_entity import BaseEntity
from server.core.types import string
from server.core.helpers.time import TimeHelper


class SubmissionLanguages(IntEnum):
    ASSEMBLY = auto()
    BASH = auto()
    BASIC = auto()
    BOSQUE = auto()
    C = auto()
    C3 = auto()
    CLOJURE = auto()
    COBOL = auto()
    COMMON_LISP = auto()
    CPP = auto()
    CPP_CLANG = auto()
    CPP_GCC = auto()
    CPP_TEST = auto()
    CPP_TEST_CLANG = auto()
    CPP_TEST_GCC = auto()
    CSHARP = auto()
    CSHARP_DOTNET = auto()
    CSHARP_MONO = auto()
    CSHARP_TEST = auto()
    C_CLANG = auto()
    C_GCC = auto()
    D = auto()
    DART = auto()
    ELIXIR = auto()
    ERLANG = auto()
    EXECUTABLE = auto()
    FORTRAN = auto()
    FSHARP = auto()
    GO = auto()
    GROOVY = auto()
    HASKELL = auto()
    JAVA = auto()
    JAVAFX = auto()
    JAVASCRIPT = auto()
    JAVA_JDK = auto()
    JAVA_OPENJDK = auto()
    JAVA_TEST = auto()
    KOTLIN = auto()
    LUA = auto()
    MPI_C = auto()
    MPI_CPP = auto()
    MPI_PYTHON = auto()
    MULTI_FILE = auto()
    NIM = auto()
    OBJECTIVE_C = auto()
    OCAML = auto()
    OCTAVE = auto()
    PASCAL = auto()
    PERL = auto()
    PHP = auto()
    PLAIN_TEXT = auto()
    PROLOG = auto()
    PYTHON = auto()
    PYTHON2 = auto()
    PYTHON2_PYPY = auto()
    PYTHON3 = auto()
    PYTHON3_PYPY = auto()
    PYTHON_FOR_ML = auto()
    PYTHON_PYPY = auto()
    R = auto()
    RUBY = auto()
    RUST = auto()
    SCALA = auto()
    SQLITE = auto()
    SWIFT = auto()
    TYPESCRIPT = auto()
    VISUAL_BASIC = auto()

    def to_language_alias(self) -> judge0.LanguageAlias:
        return judge0.LanguageAlias(self.value)


class SubmissionStatus(IntEnum):
    SUBMITTED = auto()
    PENDING = auto()
    ACCEPTED = auto()
    TIME_LIMIT_EXCEEDED = auto()
    MEMORY_LIMIT_EXCEEDED = auto()
    WRONG_ANSWER = auto()
    RUNTIME_ERROR = auto()
    COMPILE_ERROR = auto()


class SubmissionEntity(BaseEntity):
    author_id: string
    problem_id: string
    author_name: string
    title: string
    source_code: string
    language: int
    time_limit: int
    memory_limit: int
    status: int
    memory: int
    time: int

    @staticmethod
    def create(
        author_id: string,
        problem_id: string,
        author_name: string,
        source_code: string,
        title: string,
        time_limit: int,
        memory_limit: int,
        status: SubmissionStatus = SubmissionStatus.SUBMITTED,
        language: SubmissionLanguages = SubmissionLanguages.PYTHON,
        memory: int = 0,
        time: int = 0,
    ) -> "SubmissionEntity":
        return SubmissionEntity(
            id=None,
            author_id=author_id,
            problem_id=problem_id,
            author_name=author_name,
            title=title,
            source_code=source_code,
            status=status.value,
            language=language.value,
            time_limit=time_limit,
            memory_limit=memory_limit,
            memory=memory,
            time=time,
            created_at=TimeHelper.utc_timezone(),
            updated_at=TimeHelper.utc_timezone(),
            deleted_at=None,
        )
