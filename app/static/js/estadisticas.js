Highcharts.chart("lineChartContainer", {
  title: {
    text: "Cantidad de actividades por dia",
  },
  xAxis: {
    categories: [],
  },
  yAxis: {
    title: {
      text: "Cantidad",
    },
  },
  series: [
    {
      name: "Actividades",
      data: [],
    },
  ],
});

fetch("http://127.0.0.1:5000/estadisticas/cant_actividades_dia")
  .then((response) => response.json())
  .then((data) => {
    days = data.map((item) => Object.keys(item)[0]);
    values = data.map((item) => Object.values(item)[0]);

    const chart = Highcharts.charts.find(
      (chart) => chart && chart.renderTo.id === "lineChartContainer"
    );

    chart.update({
      xAxis: {
        categories: days,
      },
      series: [
        {
          data: values,
        },
      ],
    });
  })
  .catch((e) => console.error("Error:", e));

Highcharts.chart("pieChartContainer", {
  chart: {
    type: "pie",
  },
  title: {
    text: "Total de actividades por tipo",
  },
  series: [
    {
      name: "Total",
      data: [],
      size: "60%",
      innerSize: "30%",
      showInLegend: true,
      dataLabels: {
        enabled: true,
        format: "{point.name}: {point.y}",
      },
    },
  ],
});

fetch("http://127.0.0.1:5000/estadisticas/total_actividades_tipo")
  .then((response) => response.json())
  .then((data) => {
    parsedData = Object.entries(data).map(([key, value]) => ({
      name: key,
      y: value,
    }));

    const chart = Highcharts.charts.find(
      (chart) => chart && chart.renderTo.id === "pieChartContainer"
    );

    chart.update({
      series: [
        {
          data: parsedData,
        },
      ],
    });
  })
  .catch((e) => console.error("Error", e));

// const barChart = Highcharts.chart("barChartContainer", {
//   chart: {
//     type: "bar",
//   },
//   title: {
//     text: "Cantidad de actividades por mes y jornada de inicio",
//   },
//   xAxis: {
//     categories: [],
//     title: {
//       text: "Mes",
//     },
//   },
//   yAxis: {
//     min: 0,
//     title: {
//       text: "Cantidad",
//       align: "high",
//     },
//     labels: {
//       overflow: "justify",
//     },
//   },
//   series: [],
// });

// fetch("http://127.0.0.1:5000/estadisticas/actividades_jornada_mes")
//   .then((response) => response.json())
//   .then((data) => {
//     barChart.update({
//       xAxis: { categories: data.meses },
//       series: data.series,
//     });
//   })
//   .catch((e) => console.error("Error", e));
// Inicializar el gráfico de barras con Chart.js
const ctx = document.getElementById("barChartContainer").getContext("2d");
let barChart = new Chart(ctx, {
  type: "bar",
  data: {
    labels: [],
    datasets: [],
  },
  options: {
    responsive: true,
    plugins: {
      legend: {
        position: "top",
      },
      title: {
        display: true,
        text: "Cantidad de actividades por mes y jornada de inicio",
      },
    },
    scales: {
      x: {
        title: {
          display: true,
          text: "Mes",
        },
      },
      y: {
        beginAtZero: true,
        title: {
          display: true,
          text: "Cantidad",
        },
      },
    },
  },
});

fetch("http://127.0.0.1:5000/estadisticas/actividades_jornada_mes")
  .then((response) => response.json())
  .then((data) => {
    const labels = data.meses;
    const datasets = data.series.map((serie) => ({
      label: serie.name,
      data: serie.data,
    }));

    barChart.data.labels = labels;
    barChart.data.datasets = datasets;
    barChart.update();
  })
  .catch((e) => console.error("Error:", e));
