<!-- Php project to check if Hashed input matches User input. -->

<?php
    echo "Hello, project will check if a saved Hashed password matched input from a user.\n";
?> 


<?php
    // let the salt be automatically generated; not recommended
    $hashed_password = crypt('admin');
    $user_input = "admin";

    /* You should pass the entire results of crypt() as the salt for comparing a
    password, to avoid problems when different hashing algorithms are used. (As
    it says above, standard DES-based password hashing uses a 2-character salt,
    but MD5-based hashing uses 12.) */
    if (hash_equals($hashed_password, crypt($user_input, $hashed_password))) {
        echo "\nuserinput and hashed password match\n";
    }

    echo "\nHello, world!\n";

    echo "user input was:: ", $user_input, "\n";
    echo "Hashed pass was:: ", $hashed_password; 
?> 
