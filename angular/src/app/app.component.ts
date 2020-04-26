import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'angular';

  constructor(private http: HttpClient) {
    this.getPatientsProxy().subscribe();
  }

  getPatientsProxy(): Observable<any> {
    return this.http.get('/orthanc/patients');
  }

  getDogsProxy(): Observable<any> {

    return this.http.get('/api/breeds/image/random');
  }

  getDogsDirectly(): Observable<any> {
    return this.http.get('https://dog.ceo/api/breeds/image/random');
  }
}