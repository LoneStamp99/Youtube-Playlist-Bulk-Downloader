with Ada.Text_IO;

procedure Youtube is

   -- Set icon
   -- Set-ItemProperty -Path .\Youtube.ps1 -Name 'Icon' -Value 'C:\src\icon\icon.ico'

   -- Set Python path
   Python_Path : constant String := "C:\Python311\python.exe";

begin

   loop
      -- Print banner
      Ada.Text_IO.Clear_Screen;
      Ada.Text_IO.Put_Line("src/banner.py");
      Ada.Text_IO.New_Line;

      -- Print menu
      Ada.Text_IO.Put_Line("Select:");
      Ada.Text_IO.Put_Line("(1) Playlist Videos");
      Ada.Text_IO.Put_Line("(2) Playlist MP3's");
      Ada.Text_IO.Put_Line("(3) About");

      -- Prompt for user input
      Ada.Text_IO.Put("Enter your choice: ");
      Ada.Text_IO.Get_Line(Item => User_Input);

      -- Call the corresponding Python script based on the user's choice
      if User_Input = "1" then
         -- Call coreTubeVid.py
         Python_Script := "src/coreTubeVid.py";
      elsif User_Input = "2" then
         -- Call coreTubemp3.py
         Python_Script := "src/coreTubemp3.py";
      elsif User_Input = "3" then
         -- Call About.py
         Python_Script := "src/About.py";
      else
         -- Invalid choice
         Ada.Text_IO.Put_Line("Invalid choice. Please try again.");
         continue;
      end if;

      begin
         -- Call the Python script and capture the output
         -- $pythonOutput = & $pythonPath $pythonScript 2>&1
         -- Print the output from the Python script
      exception
         -- An error occurred
         when others =>
            Ada.Text_IO.Put_Line("An error occurred while executing the script: " & Exception_Message);
      end;

      -- Prompt for user input to continue or exit
      Ada.Text_IO.Put("Press Enter to continue or type 'exit' to quit: ");
      Ada.Text_IO.Get_Line(Item => User_Input);
      exit when User_Input = "exit";

   end loop;

end Youtube;
