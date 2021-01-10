import { Component, OnInit } from '@angular/core';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';
import {Router} from '@angular/router';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { BehaviorSubject, Observable } from 'rxjs';
import { ChangersService } from '../changers.service';

@Component({
  selector: 'app-ask',
  templateUrl: './ask.component.html',
  styleUrls: ['./ask.component.css']
})
export class AskComponent implements OnInit {

  askForm: FormGroup;

  constructor( 
               private readonly formBuilder: FormBuilder,
               private readonly router: Router,
               private http: HttpClient,
               private changers: ChangersService) { }

  ngOnInit(): void {
    this.askForm = this.formBuilder.group({
      ammount: ['', [Validators.nullValidator, Validators.required]],
    });
  }

  ask() {
    this.changers.addConsumer(this.askForm.value).subscribe(data => {
        
        if (data) {
          console.log(data);
        }   
      });
  }
}
