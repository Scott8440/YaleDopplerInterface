<?php
$descriptorspec = array(
 0 => array("pipe", "r"),  // stdin is a pipe that the child will read from
 1 => array("pipe", "w"),  // stdout is a pipe that the child will write to
 2 => array("file", "C:\\xampp\\htdocs\YaleDoppler\\error.txt", "a")
);

$cwd = "C:\\xampp\\htdocs\\YaleDoppler\\python";

if (isset($_REQUEST["star"])) {
  $star = $_REQUEST["star"];
}
if (isset($_REQUEST["propID"])) {
  $pID  = $_REQUEST["propID"];
}
if (isset($_REQUEST["obType"])) {
  $type = $_REQUEST["obType"];
}
if (isset($_REQUEST["mode"])) {
  $mode = $_REQUEST["mode"];
}
if (isset($_REQUEST["date"])) {
  $date = $_REQUEST["date"];
}
//Types: nInB, BI, SI, I,


if ($type == "nInB") {
  //No iodine, no Binning, with PID and star
  //TODO: Figure out what no binning means and put that back in
  $process = proc_open("python masterSearch.py -p " . $pID . " -o " . $star . " -i OUT", $descriptorspec, $pipes, $cwd);
  if (is_resource($process)) {

      echo stream_get_contents($pipes[1]);
      fclose($pipes[1]);

      $return_value = proc_close($process);
  }
}
elseif ($type == "BI") {
  //B-star with Iodine
  $process = proc_open("python masterSearch.py -p " . $pID . " -o " . $star . " -i IN", $descriptorspec, $pipes, $cwd);
  if (is_resource($process)) {

      echo stream_get_contents($pipes[1]);
      fclose($pipes[1]);

      $return_value = proc_close($process);
  }
}
elseif ($type == "SI") {
  $process = proc_open("python masterSearch.py -p " . $pID . " -o " . $star . " -i IN", $descriptorspec, $pipes, $cwd);
  if (is_resource($process)) {

      echo stream_get_contents($pipes[1]);
      fclose($pipes[1]);

      $return_value = proc_close($process);
  }
}
elseif ($type == "I") {
  $process = proc_open("python masterSearch.py -o iodine" . " -d " . $date, $descriptorspec, $pipes, $cwd);
  if (is_resource($process)) {

      echo stream_get_contents($pipes[1]);
      fclose($pipes[1]);

      $return_value = proc_close($process);
  }
}
elseif ($type == "B") {
  //B-star
  $process = proc_open("python masterSearch.py " . " -o " . $star . " -i IN", $descriptorspec, $pipes, $cwd);
  if (is_resource($process)) {
      echo $type;
      echo stream_get_contents($pipes[1]);
      fclose($pipes[1]);

      $return_value = proc_close($process);
  }
}
?>
