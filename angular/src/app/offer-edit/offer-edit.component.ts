import { Component, OnInit } from '@angular/core';
import { RestApiService } from "../shared/rest-api.service";
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-offer-edit',
  templateUrl: './offer-edit.component.html',
  styleUrls: ['./offer-edit.component.css']
})
export class OfferEditComponent implements OnInit {
  id = this.actRoute.snapshot.params['id'];
  offerData: any = {};
 
  constructor(
    public restApi: RestApiService,
    public actRoute: ActivatedRoute,
    public router: Router
  ) { 
  }

  ngOnInit() { 
    this.restApi.getOffer(this.id).subscribe((data: {}) => {
      this.offerData = data;
    })
  }

  updateOffer() {
    if(window.confirm('Are you sure, you want to update?')){
      this.restApi.updateOffer(this.id, this.offerData).subscribe(data => {
        console.log(data)
        this.router.navigate(['/offer-detail/' + this.id])
      })
    }
  }

}