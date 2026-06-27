function updateNumOfPlayers() {
    let numOfPlayers = Number(document.querySelector(".aantalspelers").value)
    console.log(numOfPlayers)
    if (numOfPlayers > 2) {
        document.querySelector(".team").style.visibility = "visible"
    } else {
        document.querySelector(".team").style.visibility = "hidden"
    }
    
}
