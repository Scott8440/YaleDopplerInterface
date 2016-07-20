<?php
   if(isset($_POST['email']))
   {
     $email = $_POST['email'];
   }
   if(isset($_POST['file1arr']))
   {
     $file1Arr = $_POST['file1arr'];
   }
   if(isset($_POST['file2arr']))
   {
     $file2Arr = $_POST['file2arr'];
   }
   if(isset($_POST['file3arr']))
   {
     $file3Arr = $_POST['file3arr'];
   }
   if(isset($_POST['dop1arr']))
   {
     $dop1Arr = $_POST['dop1arr'];
   }
   if(isset($_POST['dop2arr']))
   {
     $dop2Arr = $_POST['dop2arr'];
   }
   if(isset($_POST['tag']))
   {
     $tag = $_POST['tag']
   }
   if(isset($_POST['oldDSST']))
   {
     $oldDSST = $_POST['oldDSST'];
   }
  //  data = {'email': emailValue, 'file1arr': firstFiles, 'file2arr'
          // 'file2arr': secondFiles, 'file3arr':thirdFiles,
          // 'dop1arr': dop1Files, 'dop2Files': dop2Files};
  $descriptorspec = array(
   0 => array("pipe", "r"),  // stdin is a pipe that the child will read from
   1 => array("pipe", "w"),  // stdout is a pipe that the child will write to
   2 => array("file", "C:\\xampp\\htdocs\YaleDoppler\\error.txt", "a")
  );

  $cwd = "C:\\xampp\\htdocs\\YaleDoppler\\python";

  $process = proc_open("python process1.py", $descriptorspec, $pipes, $cwd);
  // $process = proc_open("python C:\\xampp\\htdocs\\YaleDoppler\\python\\process1.py "
  //                 .$email, $descriptorspec, $pipes, $cwd);
                  // .escapeshellarg(serialize($file1Arr)) .escapeshellarg(serialize($file2Arr))
                  // .escapeshellarg(serialize($file3Arr)) .escapeshellarg(serialize($dop1Arr))
                  // .escapeshellarg(serialize($dop2Arr)), $output);
  if (is_resource($process)) {
      // $pipes now looks like this:
      // 0 => writeable handle connected to child stdin
      // 1 => readable handle connected to child stdout
      // Any error output will be appended to /tmp/error-output.txt
      //input email
      fwrite($pipes[0], $email . "\n");
      //input 1
      foreach ($file1Arr as $file) {
        fwrite($pipes[0], $file . " ");
      }
      fwrite($pipes[0], "\n");
      //input 2
      foreach($file2Arr as $file) {
        fwrite($pipes[0], $file . " ");
      }
      fwrite($pipes[0], "\n");
      //input 3
      foreach($file3Arr as $file) {
        fwrite($pipes[0], $file . " ");
      }
      fwrite($pipes[0], "\n");
      //input 4
      foreach($dop1Arr as $file) {
        fwrite($pipes[0], $file . " ");
      }
      fwrite($pipes[0], "\n");
      //input 5
      foreach($dop2Arr as $file) {
        fwrite($pipes[0], $file . " ");
      }
      fwrite($pipes[0], "\n");
      //input 6
      fwrite($pipes[0], $tag);
      fwrite($pipes[0], "\n");
      //input 7
      fwrite($pipes[0], $oldDSST);
      fwrite($pipes[0], "\n");

      fclose($pipes[0]);
      echo stream_get_contents($pipes[1]);
      fclose($pipes[1]);
      // It is important that you close any pipes before calling
      // proc_close in order to avoid a deadlock
      $return_value = proc_close($process);
      echo "command returned $return_value\n";
}
?>
