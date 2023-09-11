$pythonPath = "C:\Python311\python.exe"
$pythonScript = ""

while ($true) {
    # Print banner
    Clear-Host

    # Run the banner.py script
    $pythonScript = "src/banner.py"
    $bannerCommand = "$pythonPath $pythonScript"
    Invoke-Expression $bannerCommand

    # Print menu
    Write-Host "`nSelect:"
    Write-Host "(1) Playlist Videos" -ForegroundColor Green
    Write-Host "(2) Playlist MP3's" -ForegroundColor Green
    Write-Host "(3) About" -ForegroundColor Red

    # Prompt for user input
    Write-Host "Enter your choice: " -NoNewline
    $choice = Read-Host

    # Call the corresponding Python script based on the user's choice
    if ($choice -eq "1") {
        $pythonScript = "src/coreTubeVid.py"
    } elseif ($choice -eq "2") {
        $pythonScript = "src/coreTubemp3.py"
    } elseif ($choice -eq "3") {
        $pythonScript = "src/About.py"
    } else {
        # Invalid choice
        Write-Host "Invalid choice. Please try again." -ForegroundColor Red
        continue
    }

    try {
        # Call the Python script using system command
        $command = "$pythonPath $pythonScript"
        Invoke-Expression $command
    } catch {
        Write-Host "An error occurred while executing the script: $_"
    }

    # Prompt to continue or exit
    Write-Host "`nPress Enter to continue or type 'exit' to quit: " -ForegroundColor Cyan
    $userInput = Read-Host

    if ($userInput -eq "exit") {
        break
    }
}

exit 0