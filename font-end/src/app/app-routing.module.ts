import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { StarterComponent } from './starter/starter.component'
import { RegisterComponent } from './register/register.component'
import { LoginComponent } from './login/login.component'
import { AskComponent } from './ask/ask.component'


const routes: Routes = [
	{path: '', component: StarterComponent},
	{path: 'login', component: LoginComponent},
	{path: 'register', component: RegisterComponent},
	{path: 'ask', component: AskComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
