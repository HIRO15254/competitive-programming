@echo off

set problemname=%1
set filename=%2
set testdir=test\%problemname%
for /f "tokens=1 delims=:_" %%a in ("%problemname%") do (
    set baseurl=%%a
)
set baseurlreplaced=%baseurl:_=-%

echo "%baseurlreplaced%" | find "past" >NUL
if not ERRORLEVEL 1 (
    set baseurlreplaced=%baseurlreplaced%-open
)

echo "%problemname%" | findstr /r "yo[1-2]" >NUL
if not ERRORLEVEL 1 (
    for /f "tokens=1,2 delims=_" %%b in ("%problemname%") do (
        set baseurlreplaced=%%b%%c

    )
)
1
rem # log in
oj login -u <<username>> -p <<password>> "https://atcoder.jp"
oj login --check "https://atcoder.jp"

rem # make test directry
if not exist %testdir% (
    oj dl -d test/%problemname%/ https://atcoder.jp/contests/%baseurlreplaced%/tasks/%problemname%
)

oj test -c "python %filename%" -d test/%problemname%/

exit