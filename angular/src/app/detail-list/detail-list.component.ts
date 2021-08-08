import { Component, OnInit } from '@angular/core';
import { RestApiService } from "../shared/rest-api.service";
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-detail-list',
  templateUrl: './detail-list.component.html',
  styleUrls: ['./detail-list.component.css']
})
export class DetailListComponent implements OnInit {
  id = this.actRoute.snapshot.params['id'];
  offerData: any = [];

  constructor(
    public restApi: RestApiService,
    public actRoute: ActivatedRoute,
    public router: Router
  ) { }

  ngOnInit() { 
    this.restApi.getOffer(this.id).subscribe((data: {}) => {
      this.offerData = data;
    })
  }

  deleteOffer(id: string) {
    if (window.confirm('Are you sure, you want to delete?')){
      this.restApi.deleteOffer(id).subscribe(data => {
        this.router.navigate(['/offers-list'])
      })
    }
  }  

}