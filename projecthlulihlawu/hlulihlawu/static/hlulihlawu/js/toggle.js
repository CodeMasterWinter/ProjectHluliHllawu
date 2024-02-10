const toggleButton = document.getElementsByClassName('toggle-button')[0]
        const navbarleft = document.getElementsByClassName('navbar-left')[0]
        const navlink = document.getElementsByClassName('nav-link')[0]
        const dropdowns = document.getElementsByClassName('dropdown')[0]

        toggleButton.addEventListener('click', () => {
            navbarleft.classList.toggle('active')
        })