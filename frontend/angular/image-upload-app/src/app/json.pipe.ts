import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'jsonPipe'
})
export class JsonPipe implements PipeTransform {
  transform(value: any): string {
    return JSON.stringify(value, null, 2);
  }
}
