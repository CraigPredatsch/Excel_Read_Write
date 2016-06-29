import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.Formatter;

/******************************************/
/***          Excel File Read           ***/
/******************************************/

public class FileWork {
    public static void main(String[] args) {


        File x = new File("C:\\Users\\predatshc\\JavaProjects\\FileTest.txt");              //File x reads from specified Excel File

        if (x.exists()) {                                                                   //If Excel file exists
            System.out.println("Your file: " + x.getName() + " exists. The file says:");    //Print this line
        }
        else {
            System.out.println("Sorry, no file found.");                                    //If not, print this line
        }

        try {
            Scanner userfile = new Scanner(x);                                              //Copies words from Excel file
            while (userfile.hasNext()) {
                System.out.println(userfile.next());                                        //Outputs word until there are none left

            }
            userfile.close();                                                               //Close file


        }

        catch (FileNotFoundException e){                                                    //Error checking
            System.out.println("Error.");
        }

        /*********************************************/
        /***          Excel File Write             ***/
        /*********************************************/

        try {
            Formatter f = new Formatter("C:\\Users\\predatshc\\JavaProjects\\FileWriteTest.txt");   //Creates a new Excel file of the given name at the given location
            f.format("%s %s %s", "1", "Jon", "Snow \r\n");                                          //Inputs strings across first row in columns A, B, and C
            f.format("%s %s %s", "2", "Daenerys", "Targaryen");                                     //Inputs strings across second row in columns A, B, and C
            f.close();                                                                              //Close file
        }
        catch (FileNotFoundException e) {                                                           //Error checking
            System.out.println("Error.");
        }

    }
}
