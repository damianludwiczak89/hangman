document.addEventListener('DOMContentLoaded', function() {

    document.querySelector('#night').onchange = function () {

    if (document.querySelector('#night').checked === true) {
        document.querySelector('#night_mode').innerHTML = "day mode";
    }
    else {
        document.querySelector('#night_mode').innerHTML = "night mode";
    }
    };

    function reset_animation(element) {

        element.style.animationName = "none";

        requestAnimationFrame(() => {
          setTimeout(() => {
            element.style.animationName = ""
          }, 0);
        });
      }

    // Set global values for stats
    if (!localStorage.getItem('won')) {
        localStorage.setItem('won', 0);
    }
    if (!localStorage.getItem('games')) {
        localStorage.setItem('games', 0);
    }
    if (!localStorage.getItem('animals_games')) {
        localStorage.setItem('animals_games', 0);
    }
    if (!localStorage.getItem('animals_won')) {
        localStorage.setItem('animals_won', 0);
    }
    if (!localStorage.getItem('countries_games')) {
        localStorage.setItem('countries_games', 0);
    }
    if (!localStorage.getItem('countries_won')) {
        localStorage.setItem('countries_won', 0);
    }
    if (!localStorage.getItem('fruits_games')) {
        localStorage.setItem('fruits_games', 0);
    }
    if (!localStorage.getItem('fruits_won')) {
        localStorage.setItem('fruits_won', 0);
    }
    if (!localStorage.getItem('vegetables_games')) {
        localStorage.setItem('vegetables_games', 0);
    }
    if (!localStorage.getItem('vegetables_won')) {
        localStorage.setItem('vegetables_won', 0);
    }
    let games = localStorage.getItem('games');
    let won = localStorage.getItem('won');
    let animals_games = localStorage.getItem('animals_games');
    let animals_won = localStorage.getItem('animals_won');
    let countries_games = localStorage.getItem('countries_games');
    let countries_won = localStorage.getItem('countries_won');
    let fruits_games = localStorage.getItem('fruits_games');
    let fruits_won = localStorage.getItem('fruits_won');
    let vegetables_games = localStorage.getItem('vegetables_games');
    let vegetables_won = localStorage.getItem('vegetables_won');

    function update_stats() {
    if (isNaN(won/games)) {
        document.querySelector("#games_stat").innerHTML = `Games: ${won}/${games} (0%)`;
    }
    else {
    document.querySelector("#games_stat").innerHTML = `Games: ${won}/${games} (${parseInt(won/games*100)}%)`;
    }

    if (isNaN(animals_won/animals_games)) {
        document.querySelector("#animals_stat").innerHTML = `Animals: ${animals_won}/${animals_games} (0%)`;
    }
    else {
        document.querySelector("#animals_stat").innerHTML = `Animals: ${animals_won}/${animals_games} (${parseInt(animals_won/animals_games*100)}%)`;
    }

    if (isNaN(countries_won/countries_games)) {
        document.querySelector("#countries_stat").innerHTML = `Countries: ${countries_won}/${countries_games} (0%)`;
    }
    else {
        document.querySelector("#countries_stat").innerHTML = `Countries: ${countries_won}/${countries_games} (${parseInt(countries_won/countries_games*100)}%)`;
    }

    if (isNaN(fruits_won/fruits_games)) {
        document.querySelector("#fruits_stat").innerHTML = `Fruits: ${fruits_won}/${fruits_games} (0%)`;
    }
    else {
        document.querySelector("#fruits_stat").innerHTML = `Fruits: ${fruits_won}/${fruits_games} (${parseInt(fruits_won/fruits_games*100)}%)`;
    }

    if (isNaN(vegetables_won/vegetables_games)) {
        document.querySelector("#vegetables_stat").innerHTML = `Vegetables: ${vegetables_won}/${vegetables_games} (0%)`;
    }
    else {
        document.querySelector("#vegetables_stat").innerHTML = `Vegetables: ${vegetables_won}/${vegetables_games} (${parseInt(vegetables_won/vegetables_games*100)}%)`;
    }
}
    update_stats();

    // Night mode toggle switch
    document.querySelector("#night").onclick = function () {
        var element = document.body;
        element.classList.toggle("dark-mode");
    }


    function new_game(){
        document.querySelector('#guess_form').style.display = "none";
        document.querySelector('#categories').style.display = "block";
        document.querySelector('#message').innerHTML = "";
        document.querySelector('#new_game').style.display = "none";
        document.querySelector('#guess').disabled = false;
        document.querySelector('#blanks').style.animationPlayState = "paused";
        document.querySelector('#input_main').style.display = "none";
        document.querySelector('#input').innerHTML = "";
        input = "";
        mistakes = 0;

    }




    fetch('/hangman_ascii/'+7+'')
    .then(response => response.json())
    .then(drawing => {
        document.querySelector('#hangman_ascii').innerHTML = drawing;
    });

    // Global variable to store the answer
    let answer;

    // Hide input field
    document.querySelector('#guess').style.display = "none";
    document.querySelector('#new_game').style.display = "none";
    document.querySelector('#input_main').style.display = "none";

    // Generate password from chosen category
    document.querySelectorAll('a').forEach(function(button) {
        button.onclick = function () {
            fetch('/generate_password/'+button.dataset.id+'')
            .then(response => response.json())
            .then(password => {
                // Set global variable answer to generated password
                answer = password;

                // Increment games played - general and for category
                games++;
                localStorage.setItem('games', games);

                if (button.dataset.id === "animals") {
                    animals_games++;
                    localStorage.setItem('animals_games', animals_games);
                }
                else if (button.dataset.id === "countries")
                {
                    countries_games++;
                    localStorage.setItem('countries_games', countries_games);
                }
                else if (button.dataset.id === "fruits") {
                    fruits_games++;
                    localStorage.setItem('fruits_games', fruits_games);
                }
                else if (button.dataset.id === "vegetables") {
                    vegetables_games++;
                    localStorage.setItem('vegetables_games', vegetables_games);
                }
                update_stats()

                // Hide categories, show input field and blank letters
                document.querySelector('#guess_form').style.display = "block";
                document.querySelector('#categories').style.display = "none";
                document.querySelector('#guess').style.display = "block";
                document.querySelector('#input_main').style.display = "block";
                let blanks = "";
                for (i = 0; i < password.length; i++) {
                    blanks += "_ ";
                }
                document.querySelector('#blanks').innerHTML = blanks;
                document.querySelector('#chosen_category').innerHTML = button.dataset.id.toUpperCase();
                // Show hangman from start form
                fetch('/hangman_ascii/'+0+'')
                .then(response => response.json())
                .then(drawing => {
                    document.querySelector('#hangman_ascii').innerHTML = drawing;

            })});
    }});

    // Mistake counter
    let mistakes = 0;
    let input = "";
    // Check if input is correct
    document.querySelector('#check').onsubmit = () =>{
        let guess = document.querySelector('#guess').value;
        let message = document.querySelector('#message');
        fetch('/check/'+answer+'/'+guess+'')
        .then(response => response.json())
        .then(response => {
            let blanks = document.querySelector('#blanks').innerHTML;
            document.querySelector('#guess').value = "";
            input = `\n${input}\n${guess}`
            document.querySelector('#input').innerHTML = input;
            // If response is 1, that means full password is guessed, and user won
            if (response === 1) {
                document.querySelector('#blanks').style.animationPlayState = "running";
                document.querySelector('#blanks').style.animationName = "grow";
                reset_animation(document.querySelector('#blanks'));
                message.innerHTML = "Congratulations, you won!";
                document.querySelector('#guess').disabled = true;
                guess = answer;

                // Update stats

                won++;
                localStorage.setItem('won', won);

                if (document.querySelector('#chosen_category').innerHTML === "ANIMALS") {
                    animals_won++;
                    localStorage.setItem('animals_won', animals_won);
                }
                else if (document.querySelector('#chosen_category').innerHTML === "COUNTRIES")
                {
                    countries_won++;
                    localStorage.setItem('countries_won', countries_won);
                }
                else if (document.querySelector('#chosen_category').innerHTML === "FRUITS") {
                    fruits_won++;
                    localStorage.setItem('fruits_won', fruits_won)
                }
                else if (document.querySelector('#chosen_category').innerHTML === "VEGETABLES") {
                    vegetables_won++;
                    localStorage.setItem('vegetables_won', vegetables_won);
                }
                update_stats()
                // show message in instead of blanks
                fetch('/blank/'+blanks+'/'+answer+'/'+guess+'')
                .then(response => response.json())
                .then(updated => {
                    document.querySelector('#blanks').innerHTML = updated;
                    document.querySelector('#new_game').style.display = "block";
                    document.querySelector('#new_game_button').onclick = function () {
                        new_game();
                        return;
                    }
                });
            }

            // If response is 2, that means user input one letter that is in the answer
            else if (response === 2) {

                // Check if this letter has already been guessed before, if it was, increment mistake and update hangman
                if (blanks.includes(guess.toUpperCase())) {
                    mistakes++;
                    fetch('/hangman_ascii/'+mistakes+'')
                    .then(response => response.json())
                    .then(drawing => {
                        document.querySelector('#hangman_ascii').innerHTML = drawing;
                        document.querySelector('#hangman_ascii').style.animationPlayState = "running";
                        document.querySelector('#hangman_ascii').style.animationName = "reset";
                        document.querySelector('#hangman_ascii').style.animationPlayState = "running";
                        document.querySelector('#hangman_ascii').style.animationName = "grow";
                        reset_animation(document.querySelector('#hangman_ascii'));

                });
                    message.innerHTML = "This letter has already been found!";

                    if (mistakes === 7) {
                        document.querySelector('#guess').disabled = true;
                        message.innerHTML = `This letter has already been found!\n You died! The answer was ${answer}`;
                        document.querySelector('#new_game').style.display = "block";
                        document.querySelector('#new_game_button').onclick = function () {
                            new_game();
                            return;
                        }
                    }
                }

                // Display blanks with the letter that user just guessed

                else {

                    document.querySelector('#blanks').style.animationPlayState = "running";
                    document.querySelector('#blanks').style.animationName = "grow";
                    reset_animation(document.querySelector('#blanks'));

                    fetch('/blank/'+blanks+'/'+answer+'/'+guess+'')
                    .then(response => response.json())
                    .then(updated => {
                        document.querySelector('#blanks').innerHTML = updated;

                        // If this was last missing letter - user has won
                        if (updated.includes("_")) {
                            message.innerHTML = "You found a letter! Keep trying! Guess another letter or full answer";
                        }
                        else {
                            message.innerHTML = "Congratulations, you won!";
                            document.querySelector('#guess').disabled = true;
                                // Update stats
                                won++;
                                localStorage.setItem('won', won);

                                if (document.querySelector('#chosen_category').innerHTML === "ANIMALS") {
                                    animals_won++;
                                    localStorage.setItem('animals_won', animals_won);
                                }
                                else if (document.querySelector('#chosen_category').innerHTML === "COUNTRIES")
                                {
                                    countries_won++;
                                    localStorage.setItem('countries_won', countries_won);
                                }
                                else if (document.querySelector('#chosen_category').innerHTML === "FRUITS") {
                                    fruits_won++;
                                    localStorage.setItem('fruits_won', fruits_won)
                                }
                                else if (document.querySelector('#chosen_category').innerHTML === "VEGETABLES") {
                                    vegetables_won++;
                                    localStorage.setItem('vegetables_won', vegetables_won);
                                }
                                update_stats()


                            document.querySelector('#new_game').style.display = "block";
                            document.querySelector('#new_game_button').onclick = function () {
                                new_game();
                                return;
                            }

                        }
                    });


                }

            }
            // Input did not match answer, update mistakes, update hangman, if mistake is 7 - game over
            else {
                mistakes++;
                fetch('/hangman_ascii/'+mistakes+'')
                .then(response => response.json())
                .then(drawing => {

                    document.querySelector('#hangman_ascii').innerHTML = drawing;
                    document.querySelector('#hangman_ascii').style.animationPlayState = "running";
                    document.querySelector('#hangman_ascii').style.animationName = "grow";
                    reset_animation(document.querySelector('#hangman_ascii'));
            });

            if (mistakes === 7) {
                document.querySelector('#guess').disabled = true;
                message.innerHTML = `No match! You died! The answer was ${answer}`;
                document.querySelector('#new_game').style.display = "block";
                document.querySelector('#new_game_button').onclick = function () {
                    new_game();
                    return;
                }
            }

            else {
                message.innerHTML = "No match! Try again! Guess a letter or full answer";
            }


            }
        });
        return false;
    };
});