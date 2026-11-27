@echo off
REM Usage: deploy.bat v2

set VERSION=%1
set CONTAINER=house-app
set IMAGE=house-price-app

if "%VERSION%"=="" (
    echo Please give a version. Example: deploy.bat v2
    exit /b 1
)

echo Step 1: Building new image %IMAGE%:%VERSION%
docker build --build-arg APP_VERSION=%VERSION% -t %IMAGE%:%VERSION% .
if errorlevel 1 (
    echo Build failed. The old container is still running.
    exit /b 1
)

echo Step 2: Stopping and removing the old container
docker stop %CONTAINER%
docker rm %CONTAINER%

echo Step 3: Starting the new container
docker run -d -p 8501:8501 --name %CONTAINER% %IMAGE%:%VERSION%

echo Step 4: Running containers
docker ps

echo Deployment of %VERSION% completed.
