import { Component, OnInit } from '@angular/core';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';
import {Router} from '@angular/router';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { BehaviorSubject, Observable } from 'rxjs';
import { ChangersService } from '../changers.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})

export class LoginComponent implements OnInit {

  loginForm: FormGroup;

  constructor( 
               private readonly formBuilder: FormBuilder,
               private readonly router: Router,
               private http: HttpClient,
               private changers: ChangersService) { }

  ngOnInit(): void {
    this.loginForm = this.formBuilder.group({
      password: ['', [Validators.nullValidator, Validators.required]],
      phone: ['', [Validators.nullValidator, Validators.required]]
    });
  }

  login() {
    this.changers.login(this.loginForm.value).subscribe(data => {
        
        if (data) {
          //console.log(data);
          localStorage.setItem('token', data['Token']);
          console.log(localStorage.getItem('token'));
        }   
      });
  }
}
