@REM %~dp0 indicates the path of the batch file so
@REM that the batch script replaces %~dp0 with
@REM whateve the path is, and therefore can find
@REM the share directory

@set "PATH=%~dp0bin;%PATH%"
@set "XTBPATH=%~dp0\share\xtb"
@set "XTB4STDAHOME=%~dp0\share\xtb4stda
@cmd