<script type="text/javascript">
var app=angular.module('Leave',[]);
app.controller('myCtrl',function($scope){
  
  $scope.ExpandNotifications=function(){
 $(".notification").style("min-width:300");
    $scope.hello="how are you";
  }
});
</script>
