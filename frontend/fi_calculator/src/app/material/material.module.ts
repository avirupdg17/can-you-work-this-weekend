import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatIconModule } from '@angular/material/icon';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatSidenavModule } from '@angular/material/sidenav';

@NgModule({
  declarations: [],
  imports: [CommonModule, MatToolbarModule, MatIconModule, MatSidenavModule],
  exports: [MatToolbarModule, MatIconModule, MatSidenavModule],
})
export class MaterialModule {}
