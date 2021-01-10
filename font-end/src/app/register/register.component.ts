import {Component, OnInit} from '@angular/core';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';
import {Router} from '@angular/router';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { BehaviorSubject, Observable } from 'rxjs';
import { ChangersService } from '../changers.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  createMemberForm: FormGroup;

  constructor(
  			private readonly formBuilder: FormBuilder,
            private readonly router: Router,
            private http: HttpClient,
            private changers: ChangersService) { }

  ngOnInit(): void {

    this.createMemberForm = this.formBuilder.group({
      name: ['', [Validators.nullValidator, Validators.required]],
      location: ['', [Validators.nullValidator, Validators.required]],
      role: ['', [Validators.nullValidator, Validators.required]],
      password: ['', [Validators.nullValidator, Validators.required]],
      phone: ['', [Validators.nullValidator, Validators.required]]

 	});

}

 	saveMember() {
   this.changers.signUp(this.createMemberForm.value).subscribe(data => {
        
        if (data) {
          console.log(data);
        }   
      });
  }
 
}

