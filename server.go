package main

import (
	"fmt"
	"log"
	"net/http"
)

func routeAddJob(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	fmt.Fprintf(w, `{"status": "Add Job"}`)
}

func routeDelJob(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	fmt.Fprintf(w, `{"status": "Del Job"}`)
}

func routeCheckCron(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	fmt.Fprintf(w, `{"status": "Check Cron"}`)
}

func routePauseJob(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	fmt.Fprintf(w, `{"status": "Pause Job"}`)
}

func main() {
	http.HandleFunc("/add_job", routeAddJob)
	http.HandleFunc("/del_job", routeDelJob)
	http.HandleFunc("/pause_job", routePauseJob)
	http.HandleFunc("/check_cron", routeCheckCron)
	log.Fatal(http.ListenAndServeTLS(":8081", "server.crt", "server.key", nil))
}
