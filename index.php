<!DOCTYPE html>

<html>
  <head>
    <title>Yale CHIRON Doppler Analysis Software</title>
    <link href = "style.css" rel="stylesheet" type="text/css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.2/jquery.min.js"></script>
    <script src="app.js"></script>

    <div class="nav">
      <ul>
        <li><a href="index.php">Home</a></li>
        <li><a href="about.html">About</a></li>
        <li><a href="contact.html">Contact</a></li>
      </ul>
    </div>
    <h1 class="main">Yale CHIRON Doppler Analysis Interface</h1>
  </head>

  <body>

    <div class="preQuestions">
      <h2>Enter one of three options</h2>
      <form method="post" name='processType' id='processType' action="process1.php" onsubmit="validateInput()">
        <ul>
          <!-- <li class="radio"><input type="radio" name="programType" onclick="document.getElementById('processType').action='process1.php';" value="ISS" checked="checked"> ISS</li>
          <li class="radio"><input type="radio" name="programType" onclick="document.getElementById('processType').action='process2.php';" value="Program"> Program</li>
          <li class="radio"><input type="radio" name="programType" onclick="document.getElementById('processType').action='process3.php';" value="Just Doppler"> Just Doppler</li> -->
          <li>PI Name: <input type="text" name="piName"></li>
          <li>Proposal ID: <input type="text" name="propID"></li>
        </ul>
        <input type="submit" name="submit">
      </form>
      <p id='validateAlert'></p>
    </div>

  </body>
</html>
