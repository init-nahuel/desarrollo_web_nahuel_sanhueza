// const labels = Utils.months({ count: 7 });
// const data = {
//   labels: labels,
//   datasets: [
//     {
//       label: "My First Dataset",
//       data: [65, 59, 80, 81, 56, 55, 40],
//       fill: false,
//       borderColor: "rgb(75, 192, 192)",
//       tension: 0.1,
//     },
//   ],
// };

const lineChart = document.getElementById("lineChart");

new Chart(lineChart, {
  type: "line",
  data: {
    labels: [
      "2024-03-30",
      "2024-03-31",
      "2024-04-01",
      "2024-04-02",
      "2024-04-03",
      "2024-04-04",
    ],
    datasets: [
      {
        label: "Actividades",
        data: [12, 19, 3, 5, 2, 3],
        borderWidth: 1,
      },
    ],
  },
  options: {
    scales: {
      y: {
        beginAtZero: true,
        title: {
          display: true,
          text: "Cantidad de Actividades",
        },
      },
    },
  },
});

const pieChart = document.getElementById("pieChart");

new Chart(pieChart, {
  type: "pie",
  data: {
    labels: ["Boxeo", "Comida", "Natacion", "Musica"],
    datasets: [
      {
        label: "Cantidad",
        data: [2, 5, 7, 2],
        backgroundColor: [
          "rgb(255, 99, 132)",
          "rgb(54, 162, 235)",
          "rgb(255, 205, 86)",
          "rgb(75, 192, 192)",
        ],
      },
    ],
  },
});

const barChart = document.getElementById("barChart");

new Chart(barChart, {
  type: "bar",
  data: {
    labels: ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"], // Meses en el eje X
    datasets: [
      {
        label: "Mañana",
        data: [5, 8, 6, 7, 4, 9], // Cantidad de actividades en la mañana
        backgroundColor: "rgba(255, 99, 132, 0.8)", // Color de las barras de la mañana
      },
      {
        label: "Mediodía",
        data: [3, 5, 4, 6, 2, 7], // Cantidad de actividades al mediodía
        backgroundColor: "rgba(54, 162, 235, 0.8)", // Color de las barras del mediodía
      },
      {
        label: "Tarde",
        data: [4, 6, 5, 8, 3, 6], // Cantidad de actividades en la tarde
        backgroundColor: "rgba(75, 192, 192, 0.8)", // Color de las barras de la tarde
      },
    ],
  },
  options: {
    responsive: true, // Hace que el gráfico sea responsivo
    plugins: {
      legend: {
        display: true, // Muestra la leyenda
        position: "top", // Posición de la leyenda
      },
    },
    scales: {
      x: {
        beginAtZero: true, // Comienza el eje X en 0
      },
      y: {
        beginAtZero: true, // Comienza el eje Y en 0
        title: {
          display: true,
          text: "Cantidad de Actividades", // Etiqueta del eje Y
        },
      },
    },
  },
});
