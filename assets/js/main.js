/**
 * Especialista en Fugas - JavaScript Core
 * Alta Ingeniería • Enrutamiento directo de leads a WhatsApp Oficial (+56 9 3223 7072)
 */

(function () {
  'use strict';

  const WHATSAPP_NUMBER = '56932237072';

  document.addEventListener('DOMContentLoaded', function () {
    initHeaderScroll();
    initMobileDrawer();
    initFaqAccordion();
    initWhatsAppForms();
  });

  // 1. Sticky Header Shadow on Scroll
  function initHeaderScroll() {
    const header = document.querySelector('.main-header');
    if (!header) return;

    window.addEventListener('scroll', function () {
      if (window.scrollY > 20) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    }, { passive: true });
  }

  // 2. Mobile Drawer Navigation
  function initMobileDrawer() {
    const toggleBtn = document.querySelector('.menu-toggle');
    const drawer = document.querySelector('.mobile-drawer');
    const backdrop = document.querySelector('.mobile-nav-backdrop');
    const closeBtn = document.querySelector('.mobile-drawer-close');

    if (!toggleBtn || !drawer || !backdrop) return;

    function openMenu() {
      toggleBtn.classList.add('open');
      drawer.classList.add('open');
      backdrop.classList.add('open');
      document.body.style.overflow = 'hidden';
    }

    function closeMenu() {
      toggleBtn.classList.remove('open');
      drawer.classList.remove('open');
      backdrop.classList.remove('open');
      document.body.style.overflow = '';
    }

    toggleBtn.addEventListener('click', function () {
      if (drawer.classList.contains('open')) {
        closeMenu();
      } else {
        openMenu();
      }
    });

    if (closeBtn) closeBtn.addEventListener('click', closeMenu);
    backdrop.addEventListener('click', closeMenu);

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && drawer.classList.contains('open')) {
        closeMenu();
      }
    });
  }

  // 3. FAQ Accordion
  function initFaqAccordion() {
    const faqItems = document.querySelectorAll('.faq-item');
    if (!faqItems.length) return;

    faqItems.forEach(function (item) {
      const questionBtn = item.querySelector('.faq-question');
      if (!questionBtn) return;

      questionBtn.addEventListener('click', function () {
        const isActive = item.classList.contains('active');

        // Close others for clean UX
        faqItems.forEach(function (other) {
          if (other !== item) {
            other.classList.remove('active');
            const otherBtn = other.querySelector('.faq-question');
            if (otherBtn) otherBtn.setAttribute('aria-expanded', 'false');
          }
        });

        if (isActive) {
          item.classList.remove('active');
          questionBtn.setAttribute('aria-expanded', 'false');
        } else {
          item.classList.add('active');
          questionBtn.setAttribute('aria-expanded', 'true');
        }
      });
    });
  }

  // 4. Send ALL Contact Forms directly to WhatsApp
  function initWhatsAppForms() {
    const forms = document.querySelectorAll('form[data-whatsapp-lead]');

    forms.forEach(function (form) {
      form.addEventListener('submit', function (e) {
        e.preventDefault();

        const nombre = form.querySelector('[name="nombre"]')?.value.trim() || 'No especificado';
        const telefono = form.querySelector('[name="telefono"]')?.value.trim() || 'No especificado';
        const comuna = form.querySelector('[name="comuna"]')?.value.trim() || 'Santiago / RM';
        const servicio = form.querySelector('[name="servicio"]')?.value || 'Emergencia Fuga de Gas / Agua';
        const mensaje = form.querySelector('[name="mensaje"]')?.value.trim() || 'Solicito atención urgente';

        const textMessage = 
`🚨 *SOLICITUD DE ATENCIÓN TÉCNICA - ESPECIALISTA EN FUGAS*
----------------------------------------
👤 *Nombre:* ${nombre}
📞 *Teléfono:* ${telefono}
📍 *Comuna / Ubicación:* ${comuna}
🔧 *Servicio:* ${servicio}
📝 *Detalle:* ${mensaje}
----------------------------------------
_Enviado desde el sitio web oficial especialista-fugas.cl_`;

        const encoded = encodeURIComponent(textMessage);
        const waUrl = `https://wa.me/${WHATSAPP_NUMBER}?text=${encoded}`;

        // Redirect directly to WhatsApp
        window.open(waUrl, '_blank');
      });
    });
  }
})();
