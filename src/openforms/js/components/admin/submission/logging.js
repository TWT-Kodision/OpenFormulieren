


const collapseLinks = document.querySelectorAll('.collapse-link');
collapseLinks.forEach(collapseLink => {
    collapseLink.textContent = collapseLink.dataset.textShow
    collapseLink.style.display = "inline"

    collapseLink.addEventListener('click', event => {
        event.preventDefault()
        if (collapseLink.parentElement.parentElement.classList.contains('collapsed')) {
            collapseLink.parentElement.parentElement.classList.remove('collapsed')
            event.target.textContent = collapseLink.dataset.textHide
        }
        else {
            collapseLink.parentElement.parentElement.classList.add('collapsed')
            event.target.textContent = collapseLink.dataset.textShow
        }
    })
})