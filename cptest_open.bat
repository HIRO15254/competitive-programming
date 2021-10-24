@echo off

set problemname=%1
set filename=%2
set testdir=test\problemname%
set charpos=0
call :find "_" "%problemname%"
set baseurl=%problemname:~0,%charpos%%
set baseurlreplaced=%baseurl:_=-%

rem # log in
oj login -u <YOUR USERNAME> -p <YOUR PASSWORD> "https://atcoder.jp"
oj login --check "https://atcoder.jp"

rem # make test directry
if not exist %testdir% (
    oj dl -d test/%problemname%/ https://atcoder.jp/contests/%baseurlreplaced%/tasks/%problemname%
)

oj test -c "python %filename%" -d test/%problemname%/

exit

:fild
    setlocal

    set find_text=%~1
    set within_text=%~2

    :label_find
    set /a charpos+=1

    if "%within_text%"=="" (
        set charpos=0
        goto :label_end
    )

    set length=0
    set str_tmp=%find_text%

    :label_strlen
    set /a length+=1
    set str_tmp=%str_tmp:~1%
    if not "%str_tmp%"=="" (goto :label_strlen)

    call set str_tmp=%%within_text:~0,%length%%%
    if "%str_tmp%"=="%find_text%" (goto :label_end)

    set within_text=%within_text:~1%
    goto :label_find

    :label_end
    endlocal && set charpos=%charpos%
exit /b