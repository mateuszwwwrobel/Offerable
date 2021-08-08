import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { MatTableModule } from '@angular/material/table';


import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { OfferCreateComponent } from './offer-create/offer-create.component';
import { OfferEditComponent } from './offer-edit/offer-edit.component';
import { OfferListComponent } from './offer-list/offer-list.component';
import { DetailListComponent } from './detail-list/detail-list.component';

@NgModule({
  declarations: [
    AppComponent,
    OfferCreateComponent,
    OfferEditComponent,
    OfferListComponent,
    DetailListComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    BrowserAnimationsModule,
    MatButtonModule,
    MatCardModule,
    MatTableModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
