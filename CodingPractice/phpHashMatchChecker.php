<!-- Php project to check if Hashed input matches User input. -->

<?php
    echo "Hello, project will check if a saved Hashed password matched input from a user.\n";
?> 

<?php
    echo "This part of the project will check the hash using the PHP Crypt() function.";
// The crypt() function returns a hashed string using DES, Blowfish, or MD5 algorithms.
    // This lets the salt be automatically generated; which is not recommended.
    $hashed_password = crypt('admin');
    $user_input = "admin";

    /* You should pass the entire results of crypt() as the salt for comparing a
    password, to avoid problems when different hashing algorithms are used. (As
    it says above, standard DES-based password hashing uses a 2-character salt,
    but MD5-based hashing uses 12.) */
    if (hash_equals($hashed_password, crypt($user_input, $hashed_password))) {
        echo "\nuserinput and hashed password match\n";
    }

    // echo "\nHello, world!\n";

    echo "user input was:: ", $user_input, "\n";
    echo "Hashed pass was:: ", $hashed_password; 
?> 
<?php
    echo "This part will check the Hash using the PHP MD5 hash() function.";
    
    if (hash('md5','240610708',false) == '0') {
        print "hash Matched ";
    }

    if ('0e953532678923638053842468642408' == '0') {
        print "Matched.n";
    }

?>