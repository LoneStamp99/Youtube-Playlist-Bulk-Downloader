#include <iostream>
#include <string>
#include <cstdlib>
#include <vector>

int main() {
    std::string pythonPath = "C:\\Python311\\python.exe";
    std::string pythonScript;

    while (true) {
        // Print banner
        system("cls");
        
        // Run the banner.py script
        pythonScript = "src/banner.py";
        std::string bannerCommand = pythonPath + " " + pythonScript;
        system(bannerCommand.c_str());


        // Print menu
        std::cout << "\nSelect:\n";
        std::cout << "(1) Playlist Videos\n";
        std::cout << "(2) Playlist MP3's\n";
        std::cout << "(3) About\n";

        // Prompt for user input
        std::cout << "Enter your choice: ";
        std::string choice;
        std::getline(std::cin, choice);

        // Call the corresponding Python script based on the user's choice
        if (choice == "1") {
            pythonScript = "src/coreTubeVid.py";
        } else if (choice == "2") {
            pythonScript = "src/coreTubemp3.py";
        } else if (choice == "3") {
            pythonScript = "src/About.py";
        } else {
            // Invalid choice
            std::cout << "Invalid choice. Please try again.\n";
            continue;
        }

        try {
            // Call the Python script using system command
            std::string command = pythonPath + " " + pythonScript;
            system(command.c_str());
        } catch (const std::exception& e) {
            std::cout << "An error occurred while executing the script: " << e.what() << "\n";
        }

        // Prompt to continue or exit
        std::cout << "\nPress Enter to continue or type 'exit' to quit: ";
        std::string userInput;
        std::getline(std::cin, userInput);

        if (userInput == "exit") {
            break;
        }
    }

    return 0;
}
