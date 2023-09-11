with Ada.Text_IO;
with Ada.Command_Line;

procedure Youtube is

   procedure Banner is
   begin
      Ada.Text_IO.Clear_Screen;
      Ada.Text_IO.Put_Line("src/banner.py");
      Ada.Text_IO.New_Line;
   end Banner;

   procedure Menu is
   begin
      Ada.Text_IO.Put_Line("Select:");
      Ada.Text_IO.Put_Line("(1) Playlist Videos");
      Ada.Text_IO.Put_Line("(2) Playlist MP3's");
      Ada.Text_IO.Put_Line("(3) About");
   end Menu;

   function Read_Choice return String is
      User_Input : String(1..100);
   begin
      Ada.Text_IO.Put("Enter your choice: ");
      Ada.Text_IO.Get_Line(Item => User_Input);
      return User_Input;
   end Read_Choice;

   procedure Execute_Python_Script(Script : String) is
      Python_Path : constant String := "C:\Python311\python.exe";
      Python_Output : String;
   begin
      Ada.Command_Line.Reset;
      Ada.Command_Line.Append(Python_Path);
      Ada.Command_Line.Append(Script);
      Ada.Command_Line.Append("2>&1");

      Ada.Command_Line.Run(Python_Output);
      Ada.Text_IO.Put_Line(Python_Output);
   end Execute_Python_Script;

   procedure Main_Loop is
      Choice : String(1..100);
      Continue : String(1..100);
   begin
      loop
         Banner;
         Menu;

         Choice := Read_Choice;

         if Choice = "1" then
            Execute_Python_Script("src/coreTubeVid.py");
         elsif Choice = "2" then
            Execute_Python_Script("src/coreTubemp3.py");
         elsif Choice = "3" then
            Execute_Python_Script("src/About.py");
         else
            Ada.Text_IO.Put_Line("Invalid choice. Please try again.");
            continue;
         end if;

         Ada.Text_IO.Put_Line("Press Enter to continue or type 'exit' to quit");
         Ada.Text_IO.Get_Line(Item => Continue);
         exit when Continue = "exit";
      end loop;
   end Main_Loop;

begin
   Main_Loop;
end Youtube;
