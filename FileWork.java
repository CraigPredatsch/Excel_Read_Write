import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.Formatter;

/******************************************/
/***          Text File Read           ***/
/******************************************/

public class FileWork {
    public static void main(String[] args) {


        File x = new File("C:\\Users\\craig\\IdeaProjects\\Java_Projects\\src\\FileTest.txt");              //File x reads from specified text File

        if (x.exists()) {                                                                   //If text file exists
            System.out.println("Your file: " + x.getName() + " exists. The file says:");    //Print this line
        }
        else {
            System.out.println("Sorry, no file found.");                                    //If not, print this line
        }

        try {
            Scanner userfile = new Scanner(x);                                              //Copies words from text file
            while (userfile.hasNext()) {
                System.out.println(userfile.next());                                        //Outputs word until there are none left

            }
            userfile.close();                                                               //Close file


        }

        catch (FileNotFoundException e){                                                    //Error checking
            System.out.println("Error.");
        }

        /*********************************************/
        /***          Text File Write             ***/
        /*********************************************/

        try {
            Formatter f = new Formatter("C:\\Users\\craig\\IdeaProjects\\Java_Projects\\src\\FileWriteTest.txt");   //Creates a new text file of the given name at the given location
            f.format("%s %s %s", "1", "Jon", "Snow \r\n");                                          //Inputs strings across first row in columns A, B, and C
            f.format("%s %s %s", "2", "Daenerys", "Targaryen");                                     //Inputs strings across second row in columns A, B, and C
            f.close();                                                                              //Close file
        }
        catch (FileNotFoundException e) {                                                           //Error checking
            System.out.println("Error.");
        }

    }
}