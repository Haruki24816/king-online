<template>
  <div class="container text-center -content">
    <div class="accordion" id="entranceAccordion">
      <div class="accordion-item">
        <h2 class="accordion-header" id="headingOne">
          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
            data-bs-target="#collapseOne">
            <i class="bi bi-door-open-fill fs-4 me-2"></i>
            部屋に入る
          </button>
        </h2>
        <div id="collapseOne" class="accordion-collapse collapse" data-bs-parent="#entranceAccordion">
          <div class="accordion-body">
            <strong>This is the first item's accordion body.</strong> It is shown by default, until the collapse
            plugin
            adds the appropriate classes that we use to style each element. These classes control the overall
            appearance,
            as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or
            overriding our default variables. It's also worth noting that just about any HTML can go within the
            <code>.accordion-body</code>, though the transition does limit overflow.
          </div>
        </div>
      </div>
      <div class="accordion-item">
        <h2 class="accordion-header" id="headingTwo">
          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
            data-bs-target="#collapseTwo">
            <i class="bi bi-plus-square-fill fs-4 me-2"></i>
            部屋を作る
          </button>
        </h2>
        <div id="collapseTwo" class="accordion-collapse collapse" data-bs-parent="#entranceAccordion">
          <div class="accordion-body">
            <strong>This is the second item's accordion body.</strong> It is hidden by default, until the collapse
            plugin
            adds the appropriate classes that we use to style each element. These classes control the overall
            appearance,
            as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or
            overriding our default variables. It's also worth noting that just about any HTML can go within the
            <code>.accordion-body</code>, though the transition does limit overflow.
          </div>
        </div>
      </div>
      <div class="accordion-item">
        <h2 class="accordion-header" id="headingThree">
          <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
            data-bs-target="#collapseThree">
            <i class="bi bi-file-text-fill fs-4 me-2"></i>
            King Online について
          </button>
        </h2>
        <div id="collapseThree" class="accordion-collapse collapse" data-bs-parent="#entranceAccordion">
          <div class="accordion-body">
            <strong>This is the third item's accordion body.</strong> It is hidden by default, until the collapse
            plugin
            adds the appropriate classes that we use to style each element. These classes control the overall
            appearance,
            as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or
            overriding our default variables. It's also worth noting that just about any HTML can go within the
            <code>.accordion-body</code>, though the transition does limit overflow.
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.-content {
  max-width: 400px;
}
</style>
