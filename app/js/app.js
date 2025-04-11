const map = document.querySelector("svg");
const countries = map.querySelectorAll("path");
const route = [];
document.querySelector('form').addEventListener('submit', function (e) {
    e.preventDefault();
    const data = Object.fromEntries(new FormData(e.target));

    if (data.countryA === data.countryB) {
        Swal.fire({
            title: "Selecciona dos paises diferentes",
            icon: "warning",
            draggable: true
        });
        return;
    }

    fetch('http://127.0.0.1:5000/dijkstra', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            first_country: data.countryA,
            second_country: data.countryB
        })
    })
        .then(response => response.json())
        .then(data => {

            if (data.error) {
                Swal.fire({
                    title: data.error,
                    icon: "error",
                    draggable: true
                });
                return;
            } else {



                route[0] = data.distance;
                route[1] = data.secuence;

                console.log(route);

                document.getElementById('distance').textContent = `${route[0]} km`;

                const resetColors = () => {
                    const allCountries = document.querySelectorAll("path");
                    allCountries.forEach(country => {
                        country.style.fill = "#373432";
                    });
                };

                resetColors();
                let index = 0;

                const changeColor = () => {
                    if (index < route[1].length) {
                        let countryName = route[1][index] || 0;
                        let countryElements;

                        countryElements = document.querySelectorAll(`[name="${countryName}"]`);

                        if (countryElements.length === 0) {
                            countryElements = document.querySelectorAll(`.${countryName.replace(/\s+/g, '.')}`);
                        }

                        if (countryElements.length > 0) {
                            countryElements.forEach(element => {
                                element.style.fill = "yellow";
                            });
                        } else {
                            console.warn(`País no encontrado en el mapa: ${countryName}`);
                        }

                        index++;
                        setTimeout(changeColor, 500);
                    }
                };

                changeColor();

                e.target.reset();
            }
        })
        .catch(error => {
            console.error('Hubo un error:', error);
        });


});