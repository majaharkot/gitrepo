<h1>Rejestracja</h1>
<p>Przesłane dane:</p>
<?php
  print_r($_GET)
  print_r($_POST)
 ?>

 <!DOCTYPE html>
 <html>
   <head>
     <meta charset="utf-8">
     <meta name="viewport" content="width=device-width, initial-scale=1">
     <meta http-equiv="x-ua-compatible" content="ie=edge">
     <title>Formularze</title>

     <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.2/css/bootstrap.min.css" integrity="sha384-y3tfxAZXuh4HwSYylfB+J125MxIs6mR5FOHamPBG064zB+AFeWH94NdvaCBm8qnd" crossorigin="anonymous">
   </head>
   <body>
     <h1>Hello, world!</h1>

     <form name="formularz" id="formularz" method="GET" action="rejestracja.php">
       <table class="table">
         <tr>
           <td>
             <label for="imie">Imię:</label>
           </td>
           <td>
             <input type="text" name="imie" value="" placeholder="Imię">
           </td>
         </tr>
         <tr>
           <td>
             <label for="nazwisko">Nazwisko:</label>
           </td>
           <td>
             <input type="text" name="nazwisko" value="" placeholder="Nazwisko">
           </td>
         </tr>

         <tr>
           <td>
             <label for="haslo">Hasło:</label>
           </td>
           <td colspan="2">
             <input type="password" name="haslo" value="">
           </td>
         </tr>

       </table>

       <!-- przyciski radio-wybór jednokrotny -->
       <label for="gender">Wybierz płeć:</label><br>
       <input type="radio" name="gender" value="male" checked> Male<br>
       <input type="radio" name="gender" value="female"> Female<br>
       <input type="radio" name="gender" value="other"> Other<br>
       <input type="radio" name="gender" value="other"> Xxx<br>

       <br>

       <!-- wybór wielokrotny -->
       <input type="checkbox" name="vehicle1" value="Bike"> I have a bike<br>
       <input type="checkbox" name="vehicle2" value="Car"> I have a car

       <!-- lista opcji -->
       <select name="cars"> <!-- multiple-lista wielokrotnego wyboru -->
         <option value="1" selected="selected">Volvo</option>
         <option value="2">Saab</option>
         <option value="3">Fiat</option>
         <option value="4">Audi</option>
       </select>

       <br>

       <textarea name="komentarz" rows="4" cols="80"></textarea>

       <br>

       <input type="submit" name="zapisz" value="Zapisz">
       <input type="reset" name="reset" value="Reset">
     </form>

     <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
     <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.2/js/bootstrap.min.js" integrity="sha384-vZ2WRJMwsjRMW/8U7i6PWi6AlO1L79snBrmgiDpgIWJ82z8eA5lenwvxbMV1PAh7" crossorigin="anonymous"></script>
   </body>
 </html>
