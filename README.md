# Dash

<br>

Utilizado para criar gráficos interativos, ou dashboards.

<br>

Com *deploy* no Heroku
- https://my-dashboard-stack.herokuapp.com

<br>

----

### Problemas

- StackOverflow: [Heroku failed to find application app error](https://stackoverflow.com/questions/60195575/heroku-failed-to-find-application-app-error)

```python
server = app.server
```

<br>

- Fechando portas abertas

```bash
lsof -i @localhost:8050
kill -9 <<PID>>
```



<br>

----

### Referências

- [How to deploy a simple Python app using nothing but Github and Heroku](https://medium.com/@austinlasseter/how-to-deploy-a-simple-plotly-dash-app-to-heroku-622a2216eb73)
- [Deploying your Dash app to Heroku - THE MAGICAL GUIDE](https://community.plotly.com/t/deploying-your-dash-app-to-heroku-the-magical-guide/46723)
