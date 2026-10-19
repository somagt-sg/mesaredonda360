(function () {
    "use strict";

    function iniciarSelectorMapa() {
        const campoLatitud = document.querySelector(
            'input[name="latitud"]'
        );

        const campoLongitud = document.querySelector(
            'input[name="longitud"]'
        );

        if (!campoLatitud || !campoLongitud) {
            return;
        }

        if (typeof L === "undefined") {
            console.error("No se pudo cargar Leaflet.");
            return;
        }

        // Evitar crear el mapa dos veces.
        if (document.getElementById("selector-mapa-negocio")) {
            return;
        }

        const filaLatitud =
            campoLatitud.closest(".form-row") ||
            campoLatitud.parentElement;

        const contenedor = document.createElement("div");
        contenedor.style.margin = "15px 0 25px";
        contenedor.style.padding = "15px";
        contenedor.style.background = "#f8fafc";
        contenedor.style.border = "1px solid #dbe3ed";
        contenedor.style.borderRadius = "10px";

        const titulo = document.createElement("h2");
        titulo.textContent = "Ubicación del negocio";
        titulo.style.margin = "0 0 8px";
        titulo.style.fontSize = "18px";
        titulo.style.color = "#172554";

        const instruccion = document.createElement("p");
        instruccion.textContent =
            "Haz clic en el mapa para colocar el punto exacto del negocio. También puedes arrastrar el marcador para corregir su ubicación.";
        instruccion.style.margin = "0 0 12px";
        instruccion.style.fontSize = "13px";
        instruccion.style.lineHeight = "1.6";
        instruccion.style.color = "#475569";

        const mapaDiv = document.createElement("div");
        mapaDiv.id = "selector-mapa-negocio";
        mapaDiv.style.width = "100%";
        mapaDiv.style.height = "420px";
        mapaDiv.style.border = "1px solid #cbd5e1";
        mapaDiv.style.borderRadius = "8px";
        mapaDiv.style.overflow = "hidden";
        mapaDiv.style.background = "#e2e8f0";

        const ayuda = document.createElement("div");
        ayuda.style.marginTop = "10px";
        ayuda.style.padding = "10px";
        ayuda.style.borderRadius = "7px";
        ayuda.style.background = "#fff7ed";
        ayuda.style.color = "#9a3412";
        ayuda.style.fontSize = "12px";
        ayuda.style.lineHeight = "1.6";
        ayuda.textContent =
            "Primero ubica el negocio en el mapa. Al seleccionar un punto, la latitud y la longitud se completarán automáticamente en el formulario.";

        contenedor.appendChild(titulo);
        contenedor.appendChild(instruccion);
        contenedor.appendChild(mapaDiv);
        contenedor.appendChild(ayuda);

        // Colocar el selector encima de los campos de coordenadas.
        if (filaLatitud && filaLatitud.parentElement) {
            filaLatitud.parentElement.insertBefore(
                contenedor,
                filaLatitud
            );
        } else {
            campoLatitud.parentElement.insertBefore(
                contenedor,
                campoLatitud
            );
        }

        const centroMesaRedonda = [-12.0478, -77.0278];

        const latitudInicial = parseFloat(campoLatitud.value);
        const longitudInicial = parseFloat(campoLongitud.value);

        const tieneCoordenadas =
            Number.isFinite(latitudInicial) &&
            Number.isFinite(longitudInicial) &&
            latitudInicial >= -90 &&
            latitudInicial <= 90 &&
            longitudInicial >= -180 &&
            longitudInicial <= 180;

        const centroInicial = tieneCoordenadas
            ? [latitudInicial, longitudInicial]
            : centroMesaRedonda;

        const zoomInicial = tieneCoordenadas ? 18 : 16;

        const mapa = L.map("selector-mapa-negocio").setView(
            centroInicial,
            zoomInicial
        );

        // Se conserva OpenStreetMap.
        L.tileLayer(
            "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
            {
                referrerPolicy: "origin",
                maxZoom: 19,
                attribution:
                    '&copy; <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener noreferrer">OpenStreetMap contributors</a>'
            }
        ).addTo(mapa);

        let marcador = null;

        function actualizarCoordenadas(latlng) {
            campoLatitud.value = latlng.lat.toFixed(7);
            campoLongitud.value = latlng.lng.toFixed(7);

            // Avisar a Django y a cualquier código del formulario.
            campoLatitud.dispatchEvent(
                new Event("change", { bubbles: true })
            );

            campoLongitud.dispatchEvent(
                new Event("change", { bubbles: true })
            );

            ayuda.textContent =
                "Punto seleccionado correctamente. Latitud: " +
                campoLatitud.value +
                " | Longitud: " +
                campoLongitud.value +
                ". Recuerda guardar el negocio.";

            ayuda.style.background = "#dcfce7";
            ayuda.style.color = "#166534";
        }

        function colocarMarcador(latlng) {
            if (marcador) {
                marcador.setLatLng(latlng);
            } else {
                marcador = L.marker(latlng, {
                    draggable: true,
                    autoPan: true
                }).addTo(mapa);

                marcador.bindPopup(
                    "Ubicación del negocio. Puedes arrastrar este punto."
                );

                marcador.on("dragend", function (evento) {
                    actualizarCoordenadas(
                        evento.target.getLatLng()
                    );
                });
            }

            actualizarCoordenadas(latlng);
        }

        // Si el negocio ya tiene ubicación, mostrar su marcador.
        if (tieneCoordenadas) {
            marcador = L.marker(centroInicial, {
                draggable: true,
                autoPan: true
            }).addTo(mapa);

            marcador.bindPopup(
                "Ubicación del negocio. Puedes arrastrar este punto."
            );

            marcador.on("dragend", function (evento) {
                actualizarCoordenadas(
                    evento.target.getLatLng()
                );
            });

            ayuda.textContent =
                "El negocio ya tiene una ubicación guardada. Haz clic en otro punto o arrastra el marcador para cambiarla.";

            ayuda.style.background = "#dcfce7";
            ayuda.style.color = "#166534";
        }

        // Cada clic sobre el mapa coloca o mueve el marcador.
        mapa.on("click", function (evento) {
            colocarMarcador(evento.latlng);
        });

        // Ajustar dimensiones cuando el navegador termina de dibujar.
        setTimeout(function () {
            mapa.invalidateSize();
        }, 250);

        window.addEventListener("resize", function () {
            mapa.invalidateSize();
        });
    }

    if (document.readyState === "loading") {
        document.addEventListener(
            "DOMContentLoaded",
            iniciarSelectorMapa
        );
    } else {
        iniciarSelectorMapa();
    }
})();