<?php

$data_file = fopen("example.txt","w"); //tries to open text if not there, make new one

$companyName = $_POST["manufacturer"];
fwrite($data_file,$companyName);
fclose($data_file);
 ?>
