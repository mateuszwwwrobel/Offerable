import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { OfferCreateComponent } from './offer-create/offer-create.component';
import { OfferEditComponent } from './offer-edit/offer-edit.component';
import { OfferListComponent } from './offer-list/offer-list.component';
import { DetailListComponent } from './detail-list/detail-list.component';

const routes: Routes = [
  { path: '', pathMatch: 'full', redirectTo: 'offers-list' },
  { path: 'create-offer', component: OfferCreateComponent },
  { path: 'offers-list', component: OfferListComponent },
  { path: 'offer-edit/:id', component: OfferEditComponent },
  { path: 'offer-detail/:id', component: DetailListComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
