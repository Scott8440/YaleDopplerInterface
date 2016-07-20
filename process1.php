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
    <pvalue="<?php echo $_POST["piName"] ?>">PI Name: <?php echo $_POST["piName"] ?></p>
    <p id="propIDp" value="<?php echo $_POST["propID"] ?>">Prop ID: <?php echo $_POST["propID"] ?></p>
  <div class="fileForm">
    <form>
      <ul id="starList">
        <li id="starLi">Star:
          <select id="starSelect" onchange="if (this.selectedIndex) selectStar(this.value)">
            <option id="none"></option>
            <?php
            $descriptorspec = array(
             0 => array("pipe", "r"),  // stdin is a pipe that the child will read from
             1 => array("pipe", "w"),  // stdout is a pipe that the child will write to
             2 => array("file", "C:\\xampp\\htdocs\YaleDoppler\\error.txt", "a")
            );

            $cwd = "C:\\xampp\\htdocs\\YaleDoppler\\python";
            $pID = $_POST["propID"];
            $process = proc_open("python starList.py " . $pID, $descriptorspec, $pipes, $cwd);
            if (is_resource($process)) {

                $starList = stream_get_contents($pipes[1]);
                echo $starList;
                fclose($pipes[1]);

                $return_value = proc_close($process);
            }
            ?>
            <script>
              function selectStar(str) {

                document.getElementById("firstListSelect1").innerHTML  = "<option>Loading...</option>";
                document.getElementById("dopList1Select1").innerHTML   = "<option>Loading...</option>";

                alreadyDSST(str);
                var pID = "<?php echo $pID ?>";
                var type = "";
                if (str.length == 0) {
                    document.getElementById("firstListSelect1").innerHTML = "";
                    return;
                }
                else {
                  var xmlhttp  = new XMLHttpRequest();
                  var xmlhttp4 = new XMLHttpRequest();

                  //No iodine, no binning
                  type = "nInB";
                  xmlhttp.open("GET", ".\\php\\updateList.php?obType="+type+"&propID="+pID+"&star="+"\""+str+"\"", true);
                  xmlhttp.send();
                  type = "SI";
                  xmlhttp4.open("GET", ".\\php\\updateList.php?obType="+type+"&propID="+pID+"&star="+"\""+str+ "\"", true);
                  xmlhttp4.send();

                  xmlhttp.onreadystatechange = function() {
                      if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
                          firstListstr = xmlhttp.responseText;
                          document.getElementById("firstListSelect1").innerHTML  = firstListstr;
                      }
                  }
                  xmlhttp4.onreadystatechange = function() {
                      if (xmlhttp4.readyState == 4 && xmlhttp4.status == 200) {
                          dopList1str = xmlhttp4.responseText;
                          document.getElementById("dopList1Select1").innerHTML   = dopList1str;
                      }
                  }
                }
            }
            function selectStar2(str)
            {

              var xmlhttp3 = new XMLHttpRequest();
              var pID = "<?php echo $pID ?>";
              var type = "";
              document.getElementById("thirdListSelect1").innerHTML  = "<option>Loading...</option>";
              document.getElementById("thirdListSelect2").innerHTML  = "<option>Loading...</option>";
              document.getElementById("thirdListSelect3").innerHTML  = "<option>Loading...</option>";

              type = "BI";
              xmlhttp3.open("GET", ".\\php\\updateList.php?obType="+type+"&propID="+pID+"&star="+"\""+str+"\"", true);
              xmlhttp3.send();

              xmlhttp3.onreadystatechange = function() {
                  if (xmlhttp3.readyState == 4 && xmlhttp3.status == 200) {
                      thirdListstr = xmlhttp3.responseText;
                      document.getElementById("thirdListSelect1").innerHTML  = thirdListstr;
                      document.getElementById("thirdListSelect2").innerHTML  = thirdListstr;
                      document.getElementById("thirdListSelect3").innerHTML  = thirdListstr;
                  }
              }
            }
            function selectStar3(str)
            {
              document.getElementById("secondListSelect1").innerHTML = "<option>Loading...</option>";

              var xmlhttp2 = new XMLHttpRequest();
              var pID = "<?php echo $pID ?>";
              var type = "";
              type = "BI";
              xmlhttp2.open("GET", ".\\php\\updateList.php?obType="+type+"&propID="+pID+"&star="+"\""+str+"\"", true);
              xmlhttp2.send();

              xmlhttp2.onreadystatechange = function() {
                  if (xmlhttp2.readyState == 4 && xmlhttp2.status == 200) {
                      secondListstr = xmlhttp2.responseText;
                      document.getElementById("secondListSelect1").innerHTML = secondListstr;
                  }
              }
            }
            function iodineSelect(observation)
            {
              //parse the date from the observation
              console.log(observation)
              var obs = (observation).split("");
              var date = obs.slice(0,6);
              date = date.join("");

              document.getElementById("dopList2Select1").innerHTML = "<option>Loading...</option>";

              var pID = "<?php echo $pID ?>";
              var type = "";

              var xmlhttp5 = new XMLHttpRequest();

              //One Iodine spectrum per night with same resolution
              type = "I";
              xmlhttp5.open("GET", ".\\php\\updateList.php?obType="+type+"&date="+date, true);
              xmlhttp5.send();

              xmlhttp5.onreadystatechange = function() {
                  if (xmlhttp5.readyState == 4 && xmlhttp5.status == 200) {
                      dopList2str = xmlhttp5.responseText;
                  }
              }
              bStar = document.getElementById("starSelectIodine").value;

              var xmlhttp6 = new XMLHttpRequest();

              type = "BI"
              xmlhttp6.open("GET", ".\\php\\updateList.php?obType="+type+"&star="+bStar+"&propID="+pID, true)
              xmlhttp6.send();

              xmlhttp6.onreadystatechange = function() {
                  if (xmlhttp6.readyState == 4 && xmlhttp6.status == 200) {
                      dopList2str += xmlhttp6.responseText;
                      document.getElementById("dopList2Select1").innerHTML = dopList2str;
                  }
              }
            }
            </script>
          </select><br><br>
          <p id='alreadyDSSTalert'></p>
          <input type="checkbox" id='alreadyDSSTbox'>
        </li>
      </ul>
    </form>
  </div>
  <div class="iss">
    <h2>Create a deconvolved stellar template observation</h2>
    <h3>Read the <a href="about.html" >documentation</a> for detailed instructions</h3>

    <h3 class="required">DSST Template Observations</h3>
    <h4>At least one observation of program star <strong>without</strong>
      the iodine cell and with no binning.</h4>
      <p>Note: If you choose more than one observation, you must choose consecutive observations from
        the same night. It is recommended to use high-resolution mode and three or more
        consecutive, iodine-free observations
      </p>
      <div class="fileForm" id="firstListDiv">
        <form>
          <ul id="firstList">
            <li id="file1">File 1:
              <select multiple id="firstListSelect1"
                onclick="checkAndDisplay(document.getElementById('firstListDiv'))">
                <option disabled>Select Star Above</option>
              </select>
            </li>
          </ul>
        </form>
        <p id="firstListInfo"></p>
      </div>

    <h3 class="required">DSST B-Star Observations</h3>
    <h4>At least three observations of a B-star <strong>with</strong>
      the iodine cell, immediately before or after the star observation</h4>
    <div class="fileForm">
      <form>
        <ul id="starList">
          <li id="starLi">Star:
            <select id="starSelect"
              onchange="if (this.selectedIndex) selectStar3(this.value)">
              <option id="none"></option>
              <?php
                  echo $starList;
              ?>
            </select>
          </li>
        </ul>
      </form>
    </div>
    <div class="fileForm" id="secondListDiv">
      <form>
        <ul id="secondList">
          <li id="file2">File 1:
            <select id="secondListSelect1" multiple
              onclick="displaySelect(document.getElementById('secondListDiv'))">
              <option disabled>Select B-star Above</option>
            </select>
          </li>
        </ul>
      </form>
      <p></p>
    </div>

    <!--<h3 class="recommended">Recommended Observations</h3>
    <h4>3 observations of a B star <strong>with</strong> the iodine cell before
      and after the star observation</h4>
      <div class="fileForm">
        <form>
          <ul id="starList">
            <li id="starLi">Star:
              <select id="starSelect" onchange="if (this.selectedIndex) selectStar2(this.value)">
                <option id="none"></option>
                <?php
                    echo $starList;
                ?>
              </select>
            </li>
          </ul>
        </form>
      </div>
    <div class="fileForm">
      <form>
        <ul id="thirdList">
          <li>Optional File:
            <select id="thirdListSelect1"></select>
          </li>
          <li>Optional File:
            <select id="thirdListSelect2"></select>
          </li>
          <li>Optional File:
            <select id="thirdListSelect3"></select>
          </li>
        </ul>
      </form>
    </div>
    <p>NOTE: The resolution mode (slit width) <strong>must</strong> be the same
      as for the template star</p>
  </div>-->

  <div class="prog">
    <h2>Create Program Observation</h2>

    <div class="required">
      <h3>Required Observations</h3>
      <h4>at least 3 observations of the star WITH the iodine cell.</h4>
      <p>NOTE: Must use the regular slit (R~90,000) and SNR > 100, no binning.</p>

      <div class="fileForm" id="dopList1Div">
        <form>
          <ul id="dopList1">
            <li id="dop1First">File 1:
              <select id="dopList1Select1" multiple
              onclick="displaySelect(document.getElementById('dopList1Div'))">
              <option disabled>Select Star Above</option>
            </select>
            </li>
          </ul>
        </form>
        <p></p>
      </div>
      <p>NOTE: It is recommended to use SNR > 150 or 200</P>
    </div>
    <div class="recommended">
      <h3>Recommended Observations</h3>
      <h4>
          Obtain one iodine spectrum or B-Star observation per night with the
          same resolution as your program observations
      </h4>
      <p>We’ll use this to get initial guesses for the wavelength solution and PSF.</p>
      <div class="fileForm">
        <form>
          <ul id="starList">
            <li id="starLi">Star:
              <select id="starSelectIodine"
                onchange="iodineSelect(getElementById('dopList1Select1').value)">
                <option id="none"></option>
                <?php
                    echo $starList;
                ?>
              </select>
            </li>
          </ul>
        </form>
      </div>
      <div class="fileForm" id="dopList2Div">
        <form>
          <ul id="dopList2">
            <li id="dop2First">Iodine Spectrum 1:
              <select id="dopList2Select1" multiple
                onclick="displaySelect(document.getElementById('dopList2Div'))">
                <option disabled>Select B-star Above</option>
              </select>
            </li>
          </ul>
        </form>
        <p></p>
      </div>
    </div>
    <button type="buton" id="dopSubmitButton" onclick="getSelectValues()">Get Select Values</button>
  </div>
  <div class="fileForm">
    <form id="emailForm">
      <li id="emailInput">Email Address: <input id="emailField" type="text" name="txt" />
      <button id="proc1Submit" type="button" value="submit">Run</button>
      <p>Please add chironinterface@gmail.com to your contact list to  prevent the email from going to spam</p>
    </form>
  </div>
</body>

</html>
