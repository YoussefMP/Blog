if (!window.formElementsLoaded) {
    document.addEventListener('DOMContentLoaded', function() {
        window.formElementsLoaded = true;
        const homeFormElements = {
            subscribeForm: document.querySelector('.subscribe-form'),
            messageForm: document.querySelector('.space-y-2'),
            subEmailInput: document.querySelector('input[name="sub-email"]'),
            msgEmailInput: document.querySelector('input[name="g-email"]'),
            messengerNameInput: document.querySelector('input[name="g-name"]'),
            msgInput: document.querySelector('textarea[name="g-msg"]'),
        };

        homeFormElements.subscribeForm.addEventListener('submit', function(event) {
            event.preventDefault();
            handleClick(homeFormElements);
        });
        homeFormElements.messageForm.addEventListener('submit', function(event) {
            event.preventDefault();
            handleClick(homeFormElements);
        });

        function handleClick(homeFromElements) {

            let emailInput;
            let activeFrom;

            if (homeFromElements.subEmailInput.value) {
                formData = new FormData();
                formData.append("subscribe-form", "");
                formData.append("sub-email", homeFromElements.subEmailInput.value);
                emailInput = homeFromElements.subEmailInput;
                activeFrom = homeFromElements.subscribeForm;
            } else if (homeFromElements.msgEmailInput.value) {
                formData = new FormData();
                formData.append("get-in-touch-form", "");
                formData.append("g-name",  homeFormElements.messengerNameInput.value);
                formData.append("g-email", homeFromElements.msgEmailInput.value);
                formData.append("g-msg",  homeFormElements.msgInput.value);
                emailInput = homeFromElements.msgEmailInput;
                activeFrom = homeFromElements.messageForm;
            }

            const csrftoken = document.getElementsByName("csrfmiddlewaretoken")[0].value

            fetch('/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-CSRFToken': csrftoken
                },
                body: new URLSearchParams(formData)
            })
            .then((response) => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then((data) => {
                if (data.error) {
                    emailInput.classList.add('is-invalid');
                    // Add code here to display the error message
                } else {
                    emailInput.classList.remove('is-invalid');
                    emailInput.classList.add("succeeded")

                     if (homeFromElements.subEmailInput.value) {
                        homeFormElements.subEmailInput.value = ''; // clear the input field
                        const successMessage = document.createElement('p');
                        successMessage.innerText = 'Thank you for subscribing!';
                        activeFrom.parentNode.replaceChild(successMessage, homeFormElements.subscribeForm);
                    } else if (homeFromElements.msgInput.value){
                        homeFormElements.messengerNameInput.value = "";
                        homeFromElements.msgEmailInput.value = "";
                        homeFormElements.msgInput.value = "";
                        showPopup("Thanks for contacting me. I will get back to you as soon as possible", 3000)
                    }
                }
            })
            .catch((error) => {
                console.error('Error:', error);
            });
        }

        function showPopup(message, timeout) {
          var popup = document.createElement("div");
          popup.classList.add("popup");
          popup.textContent = message;
          document.body.appendChild(popup);
          setTimeout(function() {
            popup.classList.remove("popup");
            setTimeout(function() {
              document.body.removeChild(popup);
            }, 1000);
          }, timeout);
        }

    });
}

