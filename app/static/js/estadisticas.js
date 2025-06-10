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
