<?php
    $fp = fopen($argv[1],"r");
  #  $fp = fopen("php://stdin","r");
    while(!feof($fp))
    {
        $buffer = trim(fgets($fp,1024));
        $new_buffer = urlencode($buffer);
        print $new_buffer."\n";
    }
    fclose($fp);
?>
